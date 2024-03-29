import requests_cache
from dotenv import dotenv_values
from datetime import datetime, timedelta
from mailer import Mailer

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

config = dotenv_values("../../.env")


def get_stock_data(stock: str = STOCK):
    stock_session = requests_cache.CachedSession(".cache/alphavantage_cache",
                                                 expire_after=10800)
    url = 'https://www.alphavantage.co/query'
    params = {
        "apikey": config.get("ALPHA_VANTAGE"),
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
    }
    r = stock_session.get(url, params)
    r.raise_for_status()
    return r.json()


def get_news(q: str = COMPANY_NAME):
    news_session = requests_cache.CachedSession(".cache/newsapi_cache",
                                                expire_after=3600)
    url = 'https://newsapi.org/v2/everything'
    date = datetime.now() - timedelta(days=1)
    params = {
        "apiKey": config.get("NEWS_API"),
        "from": date.strftime("%Y-%m-%d"),
        "sortBy": "relevancy",
        "searchIn": "title,description",
        "language": "en",
        "q": q,
    }
    r = news_session.get(url, params)
    r.raise_for_status()
    return r.json()


def percent_difference(v1: float, v2: float) -> float:
    average = (v1 + v2) / 2
    absolute_difference = v1 - v2
    percentage_change = (absolute_difference / average) * 100
    return percentage_change


stock_data = get_stock_data()
prices = stock_data["Time Series (Daily)"]
last_prices = [prices[k]["4. close"] for k in list(prices)[:2]]
difference = percent_difference(float(last_prices[-1]), float(last_prices[0]))

news_data = get_news()
articles = news_data["articles"][0:3]

title = f"{STOCK}: {"🔺" if difference > 0 else "🔻"}{difference:.2f}%"
content = "\n\n".join(
    f"{a['url']}\n{a['title']}\n{a['description']}" for a in articles)

mailer = Mailer(config["ABV_SMTP"], config["ABV_USER"], config["ABV_PASS"])
mailer.send(config["GMAIL_USER"], title, content)
