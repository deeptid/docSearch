from datetime import datetime

from search_methods.search import Search, InvalidPattern


class StringSearch(Search):
    def __init__(self, filesDataMap=None, urlContent=None):
        self.filesDataMap = filesDataMap
        self.urlContent = urlContent

    def search(self, pattern):
        if not self.isValidPattern(pattern):
            raise InvalidPattern("Invalid search term")

        print("-- String search --")
        def findAllOccurences(dataSetString):
            start = 0
            while True:
                start = dataSetString.find(pattern, start)
                if start == -1: return
                if not dataSetString[start + len(pattern)].isalnum() and (
                    (start > 0 and not dataSetString[start - 1].isalnum()) or start == 0
                ):
                    yield start
                start += len(pattern)

        if self.urlContent:
            startTime = datetime.now()
            print("{} Matches Found".format(len(list(findAllOccurences(self.urlContent)))))
        else:
            startTime = datetime.now()
            for file in self.filesDataMap:
                print("{} - {} Matches".format(file, len(list(findAllOccurences(self.filesDataMap[file])))))

        timeElapsed = datetime.now() - startTime
        print("Elapsed Time : {}".format(timeElapsed))