from urllib.request import urlopen
from bs4 import BeautifulSoup

unique_pages = set()

def getLink(articleURL):

   global unique_pages
   source = urlopen('http://en.wikipedia.org'+articleURL)
   soup = BeautifulSoup(source, 'lxml')
   try:
      print('H1->', soup.find('div', id='content').h1.text)
      print('1st Paragraph->\n', soup.find('div', id = 'mw-content-text').find('p', class_=None).text)
      print('Edit link-> ', soup.find('li', id='ca-edit').a['href'])
   except:
      print('Something is missing!')

   for link in soup.find('div', id='bodyContent').find_all('a'):
      if 'href' in link.attrs:
         if '/wiki' in link['href'] and ':' not in link['href']:
            if link['href'] not in unique_pages:
               newpage = link['href']
               print('--------------------------------------------------\nNew Page->', newpage)
               unique_pages.add(newpage)
               getLink(newpage)

getLink("")