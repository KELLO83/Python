from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path='C:\\vs code\\python\\se_module\\chromedriver.exe')

driver.get("https://www.google.com")

elem=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
elem.send_keys("모코코 이모티콘")
elem.send_keys(Keys.RETURN)
try:
    driver.implicitly_wait(time_to_wait=5)
    driver.find_element_by_xpath("""//*[@id="iur"]/div[2]/div/div/div[5]/a/g-img/div""").click()
except:
    print("오류발생")

while True:
    pass


