import requests
import datetime
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/{0}/"


def get_song_list(input_date="2000-08-12"):
    date = datetime.date.fromisoformat(input_date)
    r = requests.get(URL.format(date.strftime('%Y-%m-%d')))
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.select_one("div[class^=chart-results-list]")
    songs = content.select("div > ul > li > ul > li:first-child")
    titles = [s.find(name="h3").text.strip() for s in songs]
    artists = [s.find(name="span").text.strip() for s in songs]

    songs_list = [{"spot": i + 1, "artist": artists[i], "track": titles[i]} for
                  i in range(len(titles))]
    return songs_list
