from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://quotes.toscrape.com/page/2/').text

soup = BeautifulSoup(source, 'lxml')
csv_file = open('quotes2.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote', 'Author', 'Tags'])


for article in soup.findAll('div', class_='quote'):
    # print(article.prettify())
    try:
        quote = article.find('span', class_='text').get_text().strip()
        print(f'Quote: {quote}')
    except:
        pass
    author = article.find('small', class_='author').text.strip()
    print(f'Author: {author}')

    tags_class = article.find('div', class_='tags')
    # print(tags_class)
    tags = list()
    for tag in tags_class.find_all('a', class_='tag'):
        tags.append(tag.text.strip())
    tags = ', '.join(tags)
    print(f'Tags: {tags}')
    print('--------------------------------------------------------------------------------------')
    # print()
    csv_writer.writerow([quote, author, tags])
csv_file.close()
