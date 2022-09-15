from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome(executable_path='C:\\vs code\\python\\se_module\\chromedriver.exe')

url="https://www.google.com"
driver.get(url)

driver.find_element_by_css_selector("#gb > div > div.gb_Me > a").click()
driver.find_element_by_id("identifierId").click()
driver.find_element_by_name('identifier').send_keys("skyblizzard64")

next_1="VfPpkd-vQzf8d"
driver.find_element_by_class_name(next_1).click()





while True:
    pass