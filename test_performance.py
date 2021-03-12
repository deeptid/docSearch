import random
import string
from datetime import datetime
from timeit import timeit

from reader_service.read_files import ReadFiles
from search_methods.index_search import IndexSearch
from search_methods.re_search import RESearch
from search_methods.string_search import StringSearch

N = 7
TEST_DIR = "test_data_sets"


class TestPerformanceSearch(object):
    def __init__(self):
        self.filesDataMap = ReadFiles(TEST_DIR).readAllFilesInDir()

    def generateRandomString(self):
        res = ''.join(random.choices(string.ascii_lowercase, k=N))
        return res

    def runStringSearchPerformance(self):
        startTime = datetime.now()
        stringSearch = StringSearch(self.filesDataMap)
        for i in range(2000000):
            subString = self.generateRandomString()
            stringSearch.search(subString)

        timeElapsed = datetime.now() - startTime
        # Performance test: Elapsed Time for StringSearch: 0:01:35.766302
        print("Performance test: Elapsed Time for StringSearch: {}".format(timeElapsed))

    def runRegexSearchPerformance(self):
        startTime = datetime.now()
        rESearch = RESearch(self.filesDataMap)
        for i in range(2000000):
            subString = self.generateRandomString()
            rESearch.search(subString)

        timeElapsed = datetime.now() - startTime
        # Performance test: Elapsed Time for RegexSearch: 0:10:39.916638
        print("Performance test: Elapsed Time for RegexSearch: {}".format(timeElapsed))

    def runIndexedSearchPerformance(self):
        indexSearch = IndexSearch(self.filesDataMap)
        startTime = datetime.now()
        for i in range(2000000):
            subString = self.generateRandomString()
            indexSearch.search(subString)

        timeElapsed = datetime.now() - startTime
        # Performance test: Elapsed Time for IndexedSearch: 0:00:32.865702
        print("Performance test: Elapsed Time for IndexedSearch: {}".format(timeElapsed))