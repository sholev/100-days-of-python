from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
d = webdriver.Chrome(options=opt)
d.get("https://secure-retreat-92358.herokuapp.com/")

f_name = d.find_element(By.NAME, value="fName")
f_name.send_keys("Name")

l_name = d.find_element(By.NAME, value="lName")
l_name.send_keys("Surname")

email = d.find_element(By.NAME, value="email")
email.send_keys("email@address.com")

submit = d.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

