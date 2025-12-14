import requests
from bs4 import BeautifulSoup

url = "https://editorial.rottentomatoes.com/guide/best-thanksgiving-movies/"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

info = soup.select(".article_movie_title > h2 > a")

for movie in info:
    with open("./movies.txt", "a") as file:
        file.write(f"{info.index(movie) + 1}. {movie.getText()}\n")