import re
from datetime import datetime

from search_methods.search import Search, InvalidPattern


class RESearch(Search):
    def __init__(self, filesDataMap=None, urlContent=None):
        self.filesDataMap = filesDataMap
        self.urlContent = urlContent

    def search(self, pattern):
        if not self.isValidPattern(pattern):
            raise InvalidPattern("Invalid search term")

        print("-- Regex Search --")
        def findAllOccurences(dataSetString, pattern):
            return re.findall(pattern, dataSetString)

        regexPattern = re.compile(r'\b'+pattern+r'\b')
        if self.urlContent:
            startTime = datetime.now()
            print("{} Matches found".format(len(list(findAllOccurences(self.urlContent, regexPattern)))))
        else:
            startTime = datetime.now()
            for file in self.filesDataMap:
                print(
                    "{} - {} Matches".format(file, len(list(findAllOccurences(self.filesDataMap[file], regexPattern)))))

        timeElapsed = datetime.now() - startTime
        print("Elapsed Time : {}".format(timeElapsed))