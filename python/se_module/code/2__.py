from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


driver=webdriver.Chrome("./python./se_module/chromedriver.exe")
driver.get("http://naver.com")

elem=driver.find_element_by_class_name("link_login")
elem.click()

driver.find_element_by_id("id").send_keys("skyblizzard64")
driver.find_element_by_xpath("//*[@id='pw']").send_keys("blue8023@@") 

time.sleep(5)

driver.find_element_by_xpath("//*[@id='log.login']/span").click()

driver.find_element_by_id("id").clear()
driver.find_element_by_id("id").send_keys("skyblizzard")


print(driver.page_source) #현재페이지에 있는 모든 html 정보 출력
time.sleep(3)

driver.quit() #전체 브라우저 종료 driver.close() 현재 탭만 종료

exit()






