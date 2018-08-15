# from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
os.system('cls')

ticker = input('Ticker:')
url = 'https://in.finance.yahoo.com/quote/'+ticker+'?p='+ticker
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

labels = list()
data = list()
table = soup.find('div', id = 'quote-summary')
rows = table.find_all('tr')

for row in rows:
   labels.append(row.find_all('td')[0].text)
   data.append(row.find_all('td')[1].text)

df = pd.DataFrame({'labels':labels, 'data':data})
print(df)
df.to_csv(ticker+'.csv')