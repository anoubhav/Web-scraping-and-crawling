from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleURL):

    links_set = list()
    html = urlopen('http://en.wikipedia.org' + articleURL)
    soup = BeautifulSoup(html, 'lxml')

    for links in soup.find('div', id='bodyContent').find_all('a'):
        if 'href' in links.attrs:
            if '/wiki/' in links['href'] and ':' not in links['href']:
                links_set.append(links['href'])
    return links_set


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)]
    print(newArticle)
    links = getLinks(newArticle)
