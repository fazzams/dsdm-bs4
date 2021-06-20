import requests
from bs4 import BeautifulSoup

#1 INPUT & MOVIE URL

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
        res2 = requests.get(movieUrl)
        html2 = res2.text
        soup2 = BeautifulSoup(html2, 'html.parser')
        summary = soup2.find('div', {'class': 'credit_summary_item'})
        dirID = summary.a['href']
        dirUrl = f'https://www.imdb.com/{dirID}'
        print('Director name: ',summary.a.string)

        res3 = requests.get(dirUrl)
        html3 = res3.text
        soup3 = BeautifulSoup(html3, 'html.parser')
        knownfor = soup3.find('div', {'id': 'knownfor'})

        movieDivs = knownfor.findAll('div', {'class': 'knownfor-title'})

        for div in movieDivs:
            moviediv = div.find('div', {'class': 'knownfor-title-role'})
            print(moviediv.a.string.strip())


        break

#3 DIRECTOR'S MOVIE

# res3 = requests.get('https://www.imdb.com/name/nm0001104/?ref_=tt_ov_dr')
# html3 = res3.text
# soup3 = BeautifulSoup(html3, 'html.parser')
# knownfor = soup3.find('div', {'id': 'knownfor'})
#
# movieDivs = knownfor.findAll('div', {'class': 'knownfor-title'})
#
# for div in movieDivs:
#     moviediv = div.find('div', {'class': 'knownfor-title-role'})
#     print(moviediv.a.string.strip())


#2 DIRECTOR'S PAGE

# res2 = requests.get('https://www.imdb.com/title/tt0111161/')
# html2 = res2.text
# soup2 = BeautifulSoup(html2, 'html.parser')
#
# summary = soup2.find('div', {'class': 'credit_summary_item'})
# print(summary.a.string)
# dirID = summary.a['href']
# dirUrl = f'https://www.imdb.com/{dirID}'
# print(dirUrl)

