import re
from datetime import datetime
from search_methods.search import Search, InvalidPattern


class IndexSearch(Search):
    def __init__(self, filesDataMap=None, urlContent=None):
        self.filesDataMap = filesDataMap
        self.urlContent = urlContent
        self.cache = self.preProcess()

    def preProcess(self):
        if self.urlContent:
            cache = {}
            content = self.urlContent.replace(" ", "$")
            content = content.replace('\n', "$")
            words = re.split(r'[`\-=~!@#$%^&*()_—+\[\]{};\'\‘\\:"|<,./<>?]', content)
            for word in words:
                if word not in cache:
                    cache[word] = 1
                else:
                    cache[word] += 1
            return cache
        else:
            fileCacheMap = {}
            for file in self.filesDataMap:
                cache = {}
                content = self.filesDataMap[file].replace("\n", " ")
                content = content.replace('.', " ")
                content = content.replace(',', " ")
                content = content.replace('"', " ")
                content = content.replace('?', " ")
                content = content.replace('!', " ")
                words = content.split(" ")
                for word in words:
                    if word not in cache:
                        cache[word] = 1
                    else:
                        cache[word] += 1

                fileCacheMap[file] = cache

            return fileCacheMap

    def search(self, pattern):
        if not self.isValidPattern(pattern):
            raise InvalidPattern("Invalid search term")

        print("-- Indexed Search --")
        startTime = datetime.now()
        if self.urlContent:
            # if pattern part of a string
            # matches = list(v for k, v in self.cache.items() if self.pattern in k.lower())
            match = self.cache.get(pattern, 0)
            print("{} Matches Found".format(match))
        else:
            for file in self.cache:
                fileCache = self.cache[file]
                match = fileCache.get(pattern, 0)
                print("{} - {} Matches".format(file, match))

        timeElapsed = datetime.now() - startTime
        print("Elapsed Time : {}".format(timeElapsed))
        return timeElapsed
