from reader_service.read_files import ReadFiles
from reader_service.read_url import ReadUrl
from search_methods.index_search import IndexSearch
from search_methods.re_search import RESearch
from search_methods.string_search import StringSearch

DIR = "data_sets"


def SearchFactory(searchMethod="1", filesDataMap=None, urlContent=None):
    searchMethods = {
        "1": StringSearch,
        "2": RESearch,
        "3": IndexSearch,
    }

    return searchMethods[searchMethod](filesDataMap, urlContent)


def main():
    urlContent = None
    filesDataMap = None
    isUrl = input("Dataset Options\n1. Url \n2. Files\n")
    if isUrl == '1':
        # url = "https://en.wikipedia.org/wiki/World"
        # url = "https://en.wikipedia.org/wiki/Search_engine_technology"
        # print("Using Url {} for search\n".format(url))
        url = input("Please enter url")
        urlContent = ReadUrl(url).convertToReadable()
    else:
        print("Using Files for search\n")
        filesDataMap = ReadFiles(DIR).readAllFilesInDir()

    searchTerm = input("Enter the search term:\n")
    searchMethod = input("What would you like to use: (1) String Match (2) Regular Expressions (3) Indexed (4) All\n")
    if searchMethod != '4':
        SearchFactory(searchMethod, filesDataMap, urlContent).search(searchTerm)
    else:
        for i in range(1, 4):
            SearchFactory(str(i), filesDataMap, urlContent).search(searchTerm)


main()
