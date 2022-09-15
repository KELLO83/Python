from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome(executable_path='C:\\vs code\\python\\se_module\\chromedriver.exe')

url="https://www.naver.com"
driver.get(url)

try:
    
    driver.find_element_by_css_selector("#account > a").click()
except:
    print("--------에러발생-------------")
try:
    driver.find_element_by_css_selector("#id").send_keys("skyblizzard64")
    time.sleep(3) 
    driver.find_element_by_css_selector("#pw").send_keys("blue8023@@")
except:
    print("아이디 비번 입력 오류발생")
    
time.sleep(3)    
try:
   driver.find_element_by_class_name("btn_text").click()
except:
    print("다음버튼 누르기 오류발생")  
      
finally:
    print("자동화 시스템 완료")
while True:
    pass




