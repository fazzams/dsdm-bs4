import requests
from bs4 import BeautifulSoup

res2 = requests.get('https://www.imdb.com/title/tt0111161/')
html2 = res2.text
soup2 = BeautifulSoup(html2, 'html.parser')

summary = soup2.find('div', {'class': 'credit_summary_item'})
print(summary.a.string)
dirID = summary.a['href']
dirUrl = f'https://www.imdb.com/{dirID}'
print(dirUrl)

# movieName = input('Enter Movie Name: ')
# movieName = movieName.lower()
#
# res = requests.get('https://www.imdb.com/chart/top/')
# html = res.text
#
# soup = BeautifulSoup(html, 'html.parser')
#
# tbody = soup.find('tbody', {'class': 'lister-list'})
# trs = tbody.findAll('tr')
#
# for tr in trs:
#     td = tr.find('td', {'class': 'titleColumn'})
#     imdbMovieName = td.a.string.strip().lower()
#     if imdbMovieName == movieName:
#         movieId = td.a['href']
#         movieUrl = f'https://imdb.com/{movieId}'
#         print(movieUrl)
#         break