from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
print([tag.get_text() for tag in all_anchor_tags])
print([tag.get("href") for tag in all_anchor_tags])

heading = soup.find_all(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get_text())
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)

