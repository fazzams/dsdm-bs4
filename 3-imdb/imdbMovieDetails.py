import requests
from bs4 import BeautifulSoup

movieName = input('Enter Movie Name: ')
movieName = movieName.lower()

res = requests.get('https://www.imdb.com/chart/top/')
html = res.text

soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')

for tr in trs:
    td = tr.find('td', {'class': 'titleColumn'})
    imdbMovieName = td.a.string.strip().lower()
    if imdbMovieName == movieName:
        movieId = td.a['href']
        movieUrl = f'https://imdb.com/{movieId}'
        print(movieUrl)
        break