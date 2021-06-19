import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top/')

html = res.text

soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')

# for tr in trs:
#     td = tr.find('td', {'class': 'titleColumn'})
#     print(td.a.string, td.span.string)

with open('imdbtop.csv', 'w') as f:
    for tr in trs:
        tdn = tr.find('td', {'class': 'titleColumn'})
        tdr = tr.find('td', {'class': 'ratingColumn imdbRating'})
        f.write(tdn.a.string+ "," +tdn.span.string+ "," +tdr.strong.string)
        f.write('\n')
