from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
os.system('cls')
url = urlopen('https://twitter.com/realDonaldTrump')
soup = BeautifulSoup(url, 'lxml')
# print(soup.prettify())

profile = soup.find('div', class_ = 'ProfileHeaderCard')
try:
   print('------------------------------------------------------------------------------------------')
   print('Name:',profile.h1.a.text)
   print('Twitter handle:',profile.h1.a['href'])
   print('Bio:',profile.p.text)
   print('Location:', profile.find('div', class_ = 'ProfileHeaderCard-location').text.strip())
   print('Join date:', profile.find('div', class_ = 'ProfileHeaderCard-joinDate').find('span').next_sibling.next_sibling['title'])
   print('Latest tweet:\n', soup.find('div', class_ = 'js-tweet-text-container').p.text.strip())
   print('------------------------------------------------------------------------------------------')
except:
   print('Something is missing')

