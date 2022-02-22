from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("./python./se_module/chromedriver.exe")
driver.get("http://google.com")

try:
    
    temp=driver.find_element_by_xpath("//*[@id='input']")
except:
    print("오류발생")

temp.send_keys("모코코")




time.sleep(3)


exit()


