import requests
from bs4 import BeautifulSoup

URL = ("https://web.archive.org/web/20200518073855/https://www.empireonline"
       ".com/movies/features/best-movies-2/")

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")
html_content = (soup.find(name="main", class_="container-fluid page-content")
                .find(name="article", class_="article category--movies")
                .find(name="div", class_="article__content"))
html_titles = html_content.find_all(name="h3")
title_texts = reversed([h.get_text() for h in html_titles])

with open("movies.txt", mode="wt", encoding="utf8") as file:
    for title in title_texts:
        file.write(title + "\n")

