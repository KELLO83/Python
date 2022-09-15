from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome(executable_path='C:\\vs code\\python\\se_module\\chromedriver.exe')


driver.get("https://www.google.com")
# elem=driver.find_element_by_name("q")
try:
    elem=driver.find_element_by_class_name("gLFyf.gsfi") #gLfyf 라는 class name 과 gsfi class name이 모두들어간 class name 을찾는다 
    #css select 라는 다름 착각 금지
except:
    print("오류발생")
elem.send_keys("모코코")
elem.send_keys(Keys.RETURN)

selector = "#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a"

driver.find_element_by_css_selector(selector).click()
try:
    temp="#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img"
    driver.find_element_by_css_selector(temp).click()
except:
    print("error")
finally:
    print("자동화 진행완료") 
   

while True:
    pass