import requests
from bs4 import BeautifulSoup
from mailer import send_mail

# https://myhttpheader.com/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "sec-ch-ua": 'Google Chrome";v="123", "Not:A-Brand";v="8", '
                 '"Chromium";v="123'
}

URL = "https://www.amazon.de/en/dp/{0}"
TARGET_PRICE = 250


def get_price(product_id="B0CBYZ6DD1"):
    url = URL.format(product_id)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    right_col_html = soup.select_one("#rightCol")
    currency = right_col_html.find(name="span", class_="a-price-symbol").text
    whole = right_col_html.find(name="span", class_="a-price-whole").text
    fraction = right_col_html.find(name="span", class_="a-price-fraction").text
    number = float(f"{whole}{fraction}")
    title = soup.select_one("#productTitle").text.strip()

    return {
        "currency": currency,
        "price": number,
        "title": title,
        "id": product_id
    }


price_data = get_price()
print(price_data)
if TARGET_PRICE > price_data["price"]:
    subject = f"Price update for {price_data["id"]}"
    content = (f"Price: {price_data["currency"]}{price_data["price"]}\n"
               f"{price_data["title"]}")
    send_mail(subject, content)
