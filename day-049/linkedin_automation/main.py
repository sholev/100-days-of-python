import time
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


config = dotenv_values("../../.env")

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
d = webdriver.Chrome(options=opt)
d.get("https://www.linkedin.com/")
wait = WebDriverWait(d, 30)


def click(xpath: str):
    locator = (By.XPATH, xpath)
    wait.until(ec.element_to_be_clickable(locator)).click()


def enter(xpath: str, inp: str):
    locator = (By.XPATH, xpath)
    wait.until(ec.presence_of_element_located(locator)).send_keys(inp)


def wait_loading():
    wait.until(lambda doc: doc.execute_script(
        "return document.readyState") == "complete")


click('//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
click('//*[@id="main-content"]/div[1]/button')
enter('//*[@id="session_key"]', config["GMAIL_USER"])
enter('//*[@id="session_password"]', config["LINKEDIN_PASS"])
click('//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

d.get("https://www.linkedin.com/jobs/search")
wait_loading()
time.sleep(1)
click('/html/body/div[6]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')  # close messages
time.sleep(1)
click('//*[@id="searchFilter_workplaceType"]')
time.sleep(1)
click('/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[6]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label')
time.sleep(1)
click('/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[6]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')

wait_loading()
time.sleep(3)
enter('/html/body/div[6]/header/div/div/div/div[2]/div[1]/div/div/input[1]', 'python developer')
enter('/html/body/div[6]/header/div/div/div/div[2]/div[1]/div/div/input[1]', Keys.ENTER)
time.sleep(5)

all_listings = d.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(1)
    click('/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
    time.sleep(1)

