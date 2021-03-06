import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top/')

html = res.text

soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')

for tr in trs:
    td = tr.find('td', {'class': 'titleColumn'})
    # print(td.a.string, td.span.string)
    movieId = td.a['href']
    movieUrl = f'https://imdb.com/{movieId}'

    res2 = requests.get(movieUrl)
    html2 = res2.text
    soup2 = BeautifulSoup(html2, 'html.parser')

    info = soup2.find('div', {'class': 'subtext'})
    a = info.findAll('a')

    print(td.a.string)
    print(info.time.string.strip())
    print(a[0].string.strip())
    print(a[1].string.strip())
    print('-----------------------------')


