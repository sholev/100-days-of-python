import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def do_consent():
    base_consent = "/html/body/div[3]/div[2]/"

    consent_opt_path = base_consent + "div[1]/div[2]/div[2]/button[2]"
    click_xpath(consent_opt_path)

    consent_cnfrm_path = base_consent + "div[2]/div[3]/div[2]/button[2]"
    click_xpath(consent_cnfrm_path)

    lang_en_selector = "#langSelect-EN"
    lang_en = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, lang_en_selector)))
    ActionChains(d).move_to_element(lang_en).click(lang_en).perform()


def click_xpath(xpath):
    wait.until(ec.element_to_be_clickable((By.XPATH, xpath))).click()


def try_click_id(id_):
    try:
        wait.until(ec.presence_of_element_located((By.ID, id_))).click()
    except StaleElementReferenceException:
        wait.until(ec.presence_of_element_located((By.ID, id_))).click()


def try_upgrade():
    upgrades = d.find_elements(by=By.CSS_SELECTOR, value="div[class='crate upgrade enabled']")
    if len(upgrades) > 0:
        try:
            upgrades[-1].click()
        except StaleElementReferenceException:
            try_upgrade()


def is_complete(finish_time):
    if time.time() > finish_time:
        try:
            cookies_per_s = wait.until(ec.presence_of_element_located((By.ID, "cookiesPerSecond"))).text
        except StaleElementReferenceException:
            return is_complete(finish_time)

        print(f"cookies_per_s: {cookies_per_s}")
        return True

    return False


def convert_price(price_text: str) -> float:
    price_text = price_text.replace(".", "")
    price_text = price_text.replace(",", "")
    if " " in price_text:
        price_text = price_text.split(" ")[0]

    return float(price_text)


def buy_product():
    items = d.find_elements(by=By.CSS_SELECTOR, value="div[class='product unlocked enabled']")
    item_ids = [item.get_attribute("id") for item in items]
    prices = [convert_price(i.find_element(By.CSS_SELECTOR, "span[class='price']").text) for i in items]
    cookies = d.find_element(by=By.ID, value="cookies").text.split()[0]
    money = convert_price(cookies)
    products = {n: item_ids[n] for n in range(len(prices)) if money > prices[n]}
    if len(products) == 0:
        return

    highest_price_affordable_product = max(products)
    to_purchase_id = products[highest_price_affordable_product]
    print(f"{to_purchase_id}: {highest_price_affordable_product}")
    d.find_element(by=By.ID, value=to_purchase_id).click()


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
d = webdriver.Chrome(options=opt)
d.get("https://orteil.dashnet.org/cookieclicker/")
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
wait = WebDriverWait(d, 30, ignored_exceptions=ignored_exceptions)

do_consent()

max_check_time = 3
next_check = time.time() + max_check_time
next_five = time.time() + 60 * 5

keyboard.add_hotkey('f8', lambda: globals().update(is_clicking=not is_clicking))
is_clicking = True
while True:
    if is_clicking:
        # time.sleep(0.05)
        try_click_id("bigCookie")
    else:
        time.sleep(0.05)
        continue

    if is_complete(next_five):
        is_clicking = False
        break

    if time.time() < next_check:
        continue

    next_check = time.time() + max_check_time

    try_upgrade()
    buy_product()
    print(f"Time left: {int(next_five - time.time())}s")

