from bs4 import BeautifulSoup
import requests

r = requests.get('http://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# print(soup.title.string)
# print(soup.title.parent)
# print(soup.title.parent.name)

# for tag in soup.findAll('a'):
#     print(tag)

with open('bs4quotes.txt', 'w') as f:
    for tag in soup.findAll('span', {'class': 'text'}):
        f.write(tag.string)
        f.write('\n')

