from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
driver=webdriver.Chrome("./python./se_module/chromedriver.exe")
url="https://form.office.naver.com/form/responseView.cmd?formkey=NmY5MjA2MjctODVjYS00OGRhLThiZDAtNDU3OGVmZjMxMGQ4&sourceId=urlshare"
driver.get(url)

#학번 입력을 검색
elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[1]/div/div[3]/div/input")
elem.send_keys("12345678")

time.sleep(1)
#이름 입력을 검색
elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/input")
elem.send_keys("alpha")

time.sleep(1)
#호수 입력을 검색
elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/input")
elem.send_keys("111-111")

time.sleep(1)
try:
    driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[4]/div/div[3]/div/div[2]/div").send_keys(Keys.ENTER)
except:
    print(err)
    print("1")
time.sleep(1)

try:
    elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[6]/div/div[3]/div/div[9]/div")
    elem.send_keys(Keys.ENTER)
except:
    print(err)
    print("2")    


try:    
    elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[7]/div/div[3]/div/div[2]/div")
    driver.implicitly_wait(10)
    elem.send_keys(Keys.ENTER)
except Exception as err:
    print(err)
    print("3")


try:
    elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/form/div/div[8]/div/div[3]/div/input")
    elem.send_keys("36.5")
except:
    print("err")
    print("4")
    
time.sleep(1.5)

try:
    elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div[2]/div/div/div[2]/div/button[3]")
    elem.send_keys(Keys.ENTER)
    
except Exception as err:
    print(err)
    print("5")

time.sleep(5)

print(datetime.datetime.today())

while True:
    pass




