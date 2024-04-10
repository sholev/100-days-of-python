from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
d = webdriver.Chrome(options=opt)
d.get("https://en.wikipedia.org/wiki/Main_Page")


articles_count = d.find_element(By.CSS_SELECTOR, "#articlecount > a")
print(articles_count.text)

all_portals = d.find_element(By.LINK_TEXT, value="Content portals")
print(all_portals.location)

search = d.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

