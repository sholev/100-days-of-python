from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(r.text, "html.parser")

print(soup.title)
html_titles = soup.find_all(name="span", class_="titleline")
print(html_titles)

titles = [html.find(name="a").get_text() for html in html_titles]
links = [html.find(name="a").get("href") for html in html_titles]
print(titles)
print(links)

html_scores = soup.find_all(name="span", class_="score")
scores = [int(html.get_text().split()[0]) for html in html_scores]
print(scores)

index = scores.index(max(scores))

print(index)
print(titles[index])
print(links[index])
print(scores[index])
