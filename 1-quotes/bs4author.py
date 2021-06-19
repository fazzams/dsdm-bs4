from bs4 import BeautifulSoup
import requests

r = requests.get('http://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

with open('authorbs4.csv', 'w') as f:
    for tag in soup.findAll('small', {'class': 'author'}):
        f.write(tag.string)
        f.write('\n')