from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome(executable_path='C:\\vs code\\python\\se_module\\chromedriver.exe')

url="https://www.naver.com"
driver.get(url)

elem=driver.find_element_by_name("query")
elem.send_keys("모코코")
elem.send_keys(Keys.RETURN)


driver.find_element_by_xpath("""//*[@id="lnb"]/div[1]/div/ul/li[2]/a""").click()

driver.find_element_by_xpath("""//*[@id="snb"]/div[3]/div/div[1]/div[3]/a/span""").click()    
    

        
while True:
    pass




