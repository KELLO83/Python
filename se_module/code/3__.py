from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("./python./se_module/chromedriver.exe")
driver.get("http://naver.com")

elem=driver.find_element_by_id("query")
elem.send_keys("네이버 항공권")
elem.send_keys(Keys.ENTER)

# 페이지 로딩이 완료되는지 확인 하기.
token  = "/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/p"    
try:    
    rvalue = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,token))
        )
    
    print("리턴값.", rvalue)
except Exception as e:
    print("오류발생.", e )
    driver.quit()
    
# # 페이지 로깅이 완료된것을 확인 한후 1초 있다가.....하고 싶은거.    
# time.sleep(1)
driver.find_element_by_xpath(token).click()


while True:
    pass


