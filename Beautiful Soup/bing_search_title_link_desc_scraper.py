from bs4 import BeautifulSoup
import requests
import os
os.system('cls')

search = input('''----------------------------------------------------------------------------
----------------------------------------------------------------------------\nSearch for:''')
params = {'q': search}
html = requests.get('http://www.bing.com/search', params = params)

soup = BeautifulSoup(html.text, 'lxml')
results = soup.find('ol', {'id':'b_results'})
# print(results.prettify())
pages = results.find_all('li', {'class':'b_algo'})
# print(pages.prettify())
for item in pages:
   try:
      title = item.find('a').text
      link = item.find('a')['href']
      description = item.find('div', {'class':'b_snippet'}).find('p').text
      
   except:
      pass
      
   if title and link and description:
      print(title)
      print(link)
      print('Parent:', item.find('a').parent)
      print('Description:', description)
      print('-----------------------------------------------------------------------------------------------------------')

