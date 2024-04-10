import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
d = webdriver.Chrome(options=opt)
d.get("https://orteil.dashnet.org/cookieclicker/")
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
wait = WebDriverWait(d, 30, ignored_exceptions=ignored_exceptions)

consent_opt_path = "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[2]"
wait.until(ec.element_to_be_clickable((By.XPATH, consent_opt_path)))
consent_opt = d.find_element(By.XPATH, consent_opt_path)
consent_opt.click()

consent_cnfrm_path = "/html/body/div[3]/div[2]/div[2]/div[3]/div[2]/button[2]"
consent_cnfrm = d.find_element(By.XPATH, consent_cnfrm_path)
consent_cnfrm.click()

lang_en_selector = "#langSelect-EN"
lang_en = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                     lang_en_selector)))
ActionChains(d).move_to_element(lang_en).click(lang_en).perform()

cookie = wait.until(ec.presence_of_element_located((By.ID, "bigCookie")))

max_check_time = 10
next_check = time.time() + max_check_time
next_five = time.time() + 60 * 5

while True:
    try:
        cookie.click()
    except StaleElementReferenceException as e:
        cookie = wait.until(
            ec.presence_of_element_located((By.ID, "bigCookie")))
        cookie.click()

    if time.time() > next_five:
        cookies_per_s = wait.until(
            ec.presence_of_element_located((By.ID, "cookiesPerSecond"))).text
        print(f"cookies_per_s: {cookies_per_s}")
        break

    if time.time() < next_check:
        continue

    next_check = time.time() + randint(1, max_check_time)

    upgrades = d.find_elements(by=By.CSS_SELECTOR,
                               value="div[class='crate upgrade enabled']")
    if len(upgrades) > 0:
        upgrades[-1].click()

    items = d.find_elements(by=By.CSS_SELECTOR,
                            value="div[class='product unlocked enabled']")
    item_ids = [item.get_attribute("id") for item in items]

    prices = [float(
        item.find_element(By.CSS_SELECTOR, "span[class='price']").text.replace(
            ",", "")) for item in items]

    cookies = d.find_element(by=By.ID, value="cookies").text.split()[0]
    money = float(cookies.replace(",", ""))
    products = {n: item_ids[n] for n in range(len(prices)) if
                money > prices[n]}

    if len(products) == 0:
        continue

    highest_price_affordable_product = max(products)
    to_purchase_id = products[highest_price_affordable_product]
    print(f"{to_purchase_id}: {highest_price_affordable_product}")
    d.find_element(by=By.ID, value=to_purchase_id).click()
