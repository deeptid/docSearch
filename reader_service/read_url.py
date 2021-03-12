from urllib.request import urlopen
from bs4 import BeautifulSoup


class ReadUrl(object):
    def __init__(self, url):
        self.url = url

    def convertToReadable(self):
        page = urlopen(self.url)
        htmlPage = BeautifulSoup(page, 'html.parser')
        article_paragraphs = htmlPage.find_all('p')
        content = ''
        for para in article_paragraphs:
            content += para.text

        return content.strip().lower()