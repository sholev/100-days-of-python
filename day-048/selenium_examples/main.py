from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def close_driver(driver):
    # driver.close()  # close tab
    driver.quit()  # close browser


def get_amazon_price(url="https://www.amazon.de/en/dp/{0}", p_id="B0CBYZ6DD1"):
    driver = get_driver()
    driver.get(url.format(p_id))
    whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    print(f"Price: {whole.text}.{fraction.text}")

    close_driver(driver)


def get_python_org_elements(url="https://www.python.org/"):
    driver = get_driver()
    driver.get(url)
    search_bar = driver.find_element(By.NAME, value="q")
    print(search_bar.get_attribute("placeholder"))
    button = driver.find_element(By.ID, value="submit")
    print(button.size)
    doc = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    print(doc.text)
    xpath = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
    bug_link = driver.find_element(By.XPATH, value=xpath)
    print(bug_link.text)

    close_driver(driver)


def get_python_upcoming_events(url="https://www.python.org/"):
    d = get_driver()
    d.get(url)
    times = d.find_elements(By.CSS_SELECTOR, '.event-widget time')
    events = d.find_elements(By.CSS_SELECTOR, '.event-widget li a')
    result = {i: {"name": events[i].text, "time": times[i].text} for i in
              range(len(times))}

    print(result)
    close_driver(d)




