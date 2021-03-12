import io
import unittest
import unittest.mock

from reader_service.read_files import ReadFiles
from search_methods.index_search import IndexSearch
from search_methods.re_search import RESearch
from search_methods.search import InvalidPattern
from search_methods.string_search import StringSearch

TEST_DIR = "test_data_sets"


class TestBaseSearch(unittest.TestCase):
    def setUp(self):
        self.filesDataMap = ReadFiles(TEST_DIR).readAllFilesInDir()


class TestStringSearch(TestBaseSearch):
    def testpatternWithSpecialCharacters(self):
        stringSearch = StringSearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            stringSearch.search("the%^*&@^#")

    def testpatternWithSpaces(self):
        stringSearch = StringSearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            stringSearch.search("the the")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testPatternNotFound(self, mock_stdout):
        stringSearch = StringSearch(self.filesDataMap)
        stringSearch.search("PacificPacificPacific")
        self.assertIn("0 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testStringSearch(self, mock_stdout):
        stringSearch = StringSearch(self.filesDataMap)
        stringSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())


class TestRegexSearch(TestBaseSearch):
    def testpatternWithSpecialCharacters(self):
        reSearch = RESearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            reSearch.search("the%^*&@^#")

    def testpatternWithSpaces(self):
        reSearch = RESearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            reSearch.search("the the")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testPatternNotFound(self, mock_stdout):
        reSearch = RESearch(self.filesDataMap)
        reSearch.search("PacificPacificPacific")
        self.assertIn("0 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testRegexSearch(self, mock_stdout):
        reSearch = RESearch(self.filesDataMap)
        reSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())

class TestIndexedSearch(TestBaseSearch):
    def testpatternWithSpecialCharacters(self):
        indexSearch = IndexSearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            indexSearch.search("the%^*&@^#")

    def testpatternWithSpaces(self):
        indexSearch = IndexSearch(self.filesDataMap)
        with self.assertRaises(InvalidPattern):
            indexSearch.search("the the")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testPatternNotFound(self, mock_stdout):
        indexSearch = IndexSearch(self.filesDataMap)
        indexSearch.search("PacificPacificPacific")
        self.assertIn("0 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testIndexSearch(self, mock_stdout):
        indexSearch = IndexSearch(self.filesDataMap)
        indexSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())


class TestPatternSearch(unittest.TestCase):
    def setUp(self):
        self.filesDataMap = ReadFiles(TEST_DIR).readAllFilesInDir()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testStringSearch(self, mock_stdout):
        stringSearch = StringSearch(self.filesDataMap)
        stringSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testStringSearch(self, mock_stdout):
        stringSearch = StringSearch(self.filesDataMap)
        stringSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testRegexSearch(self, mock_stdout):
        reSearch = RESearch(self.filesDataMap)
        reSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testIndexedSearch(self, mock_stdout):
        indexSearch = IndexSearch(self.filesDataMap)
        indexSearch.search("the")
        self.assertIn("62 Matches", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()