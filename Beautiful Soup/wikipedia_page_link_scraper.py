from urllib.request import urlopen
from bs4 import BeautifulSoup

links_set = list()
articleURL = '/wiki/Kevin_Bacon'
html = urlopen('http://en.wikipedia.org' + articleURL)
soup = BeautifulSoup(html, 'lxml')

for links in soup.find('div', id='bodyContent').find_all('a'):
    if 'href' in links.attrs:
        if '/wiki/' in links['href'] and ':' not in links['href']:
            links_set.append('http://en.wikipedia.org' + links['href'])
            print('http://en.wikipedia.org' + links['href'])
