from requests import get
from bs4 import BeautifulSoup

search_url = "https://www.imdb.com/search/title/?title={0}&title_type=feature"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "sec-ch-ua": 'Google Chrome";v="123", "Not:A-Brand";v="8", '
                 '"Chromium";v="123'
}


def search(title: str):
    url = search_url.format(title)
    r = get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    soup.select_one(
        '#__next > main > div.ipc-page-content-container.ipc-page-content'
        '-container--center.sc-dec63aac-0.uHlFE > '
        'div.ipc-page-content-container.ipc-page-content-container--center > '
        'section > section > div > section > section > div:nth-child(2) > '
        'div > section > div.ipc-page-grid.ipc-page-grid--bias-left.ipc-page'
        '-grid__item.ipc-page-grid__item--span-2 > '
        'div.ipc-page-grid__item.ipc-page-grid__item--span-2 > ul')
    lis = soup.find_all(name="li", class_="ipc-metadata-list-summary-item")
    result = []
    for li in lis:
        try:
            title = li.find(name="h3", class_="ipc-title__text")
            year = li.select_one(f'{'div >' * 6} span')
            description = li.find(name="div",
                                  class_="ipc-html-content-inner-div")
            rating = li.select_one(f'{'div >' * 5} span > div > span')
            img = li.find('img')['src']
            # img = img.split("@")[0] + '@._V1_FMjpg_UY1200_.jpg'
            result.append({
                'title': title.text.split('.', 1)[1],
                'year': int(year.text),
                'description': description.text,
                'rating': rating.contents[1].text,
                'img_url': img,
                'ranking': "",
                'review': "",
            })
        except:
            pass

    return result

