from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


driver=webdriver.Chrome("./python./se_module/chromedriver.exe")

url="http://naver.com"
driver.get(url)


elem=driver.find_element_by_id("query")
elem.send_keys("모코코")
elem.send_keys(Keys.ENTER)


temp=driver.find_element_by_tag_name("a")

print(temp)

    
driver.get("http://daum.net")

elem=driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div[1]/form/fieldset/div/div/input")

elem.send_keys("모코코")
elem.send_keys(Keys.ENTER)

driver.back()

driver.close()

exit()


    
    




