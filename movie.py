import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_data = []

movies = soup.select('dt.tit a')
for a_tag in movies:
    title = a_tag.text

    link_split = a_tag['href'].split('=')
    code = link_split[1]
    movie_tile_code = {
        'title' : title,
        'code' : code
    }
    movie_data.append(movie_tile_code)

for name in movie_data:
    print(name['title'] + "/"+ name['code'])