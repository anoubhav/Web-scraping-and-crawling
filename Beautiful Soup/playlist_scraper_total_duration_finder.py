from bs4 import BeautifulSoup
import requests
import string
import re
playlist_link = 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF'

source = requests.get(playlist_link).text
mins = 0
seconds = 0
soup = BeautifulSoup(source, 'lxml')
durations = list()
# article = soup.find('div', id='contents')
for span in soup.find_all('span'):
    if 'aria-label' in span.attrs:
        if 'minutes' in span['aria-label']:
            durations.append(span['aria-label'])
print(durations)
for time in durations:
    a = re.findall('[0-9]+', time)
    # print(a[0])
    mins += int(a[0])
    try:
        seconds += int(a[1])
    except:
        continue
print(mins, seconds)
tot = (mins + seconds / 60) / 60
print('Total duration in hrs: {:.2f}'.format(tot))
