import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome(executable_path="./python./se_module/chromedriver.exe")

url="https://finance.daum.net/quotes/A205470#current/quote" 

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/97.0.4692.71 Safari/537.36"}

res=requests.get(url,headers=headers)
                                                                                                                          
if res.status_code==requests.codes.ok:
    print("정상")
else:
    print(f"문제 발생 에러코드{res.status_code}")
    
driver.implicitly_wait(10)  #페이지의 모든요소가 로드될때까지 최대 10초기다린다 모든 요소들이 나오면 이전에 종료됨
driver.get(url)
page=driver.page_source #selenium이용한 html 정보 가져오기 정적인정보까지 모두가져옴
soup=BeautifulSoup(page,"lxml")  #html.passer    
    


# v2=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents") #CSS_Selector 를 이용한 elem찾기
# f2=soup.select_one("#boxDayHistory > div.tableB.selectTop.pt0") #CSS_Selector를 이용한 다중  class name찾기 
# f1=soup.find("div",class_="box_contents") #class name을가지고 찾기 class명이 table B,selectTop,pt0 모두 해당되는 class name 이다 table B클래스를 찾은이후 SelectTop pt0를 찾을려고할경우 찾지못한다


    
    
# r1=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents > div")
   
# r2=r1.get_attribute('innerHTML') #seleniunm을 이용한 전체 문서의html정보가 아닌 일부요소의 html정보를 가져오기
   
# s1=BeautifulSoup(r2,"lxml") #r2는 selenium에서 얻어온것이므로 다시 bs4가 읽을수있는 형태로 바꿔준다

# s2=s1.find("tr",class_="first") #s2 는인수



# date=s2.select_one("span:nth-of-type(1)") #span태그가붙어있는것중에 첫번쨰
# date2=s2.select_one(".time:nth-of-type(1)") #class name 이 time 중 첫번쨰
"""
<tr class="first">
<td><span class="time">22.01.28</span></td>
<td><span class="num">82,800</span></td>
<td><span class="num">85,600</span></td>
<td><span class="num">82,200</span></td>
<td><span class="num">85,000</span></td>
<td><span class="num up"><i>▲</i>2,400</span></td>
<td><span class="num up">+2.91%</span></td>
<td class="pR"><span class="num">2,943,023</span></td>
</tr>
"""


"""
<tr class="">
<td><span class="time">22.01.27</span></td>
<td><span class="num">87,000</span></td>
<td><span class="num">87,500</span></td>
<td><span class="num">82,600</span></td>
<td><span class="num">82,600</span></td>
<td><span class="num down"><i>▼</i>4,300</span></td>
<td><span class="num down">-4.95%</span></td>
<td class="pR"><span class="num">3,793,749</span></td>
</tr>
"""

def find():
    count=0
    r1=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents > div")
    r2=r1.get_attribute('innerHTML') #seleniunm을 이용한 전체 문서의html정보가 아닌 일부요소의 html정보를 가져오기
    s1=BeautifulSoup(r2,"lxml") #r2는 selenium에서 얻어온것이므로 다시 bs4가 읽을수있는 형태로 바꿔준다
    elem=s1.find("tr",class_="first") #s2 는인수
    
    while(count<10):
        TIME_DATE=elem.select_one("td:nth-of-type(1)")
        TIME_DATE=elem.select_one("td:nth-of-type(1)")
        SELLING_PRICE_RULING_TIME=elem.select_one("td:nth-of-type(2)") #nth:of:tpye(n) 은 only table tag 사용가능 <td>/<tr>
        HIGH=elem.select_one("td:nth-of-type(3)")
        LOW_COST=elem.select_one("td:nth-of-type(4)")
        CLOSING_PRICE=elem.select_one("td:nth-of-type(5)")
        print("==== 날짜{}   시가{}   고가{}   저가{}   종가{} ====".format(TIME_DATE.string,SELLING_PRICE_RULING_TIME.string,HIGH.string,LOW_COST.string,CLOSING_PRICE.string))
        count+=1
        
        k1=SELLING_PRICE_RULING_TIME.string.replace(",","")
        k2=HIGH.string.replace(",","")
        k3=LOW_COST.string.replace(",","")
        k4=CLOSING_PRICE.string.replace(",","")
        
        
        
        with open("종목명.txt","a",encoding="utf-8") as f:
            f.write(TIME_DATE.string)
            f.write(",{}".format(k1))
            f.write(",{}".format(k2))
            f.write(",{}".format(k3))
            f.write(",{}".format(k4))
            f.write("\n")
        
        if count!=10:
            elem=elem.find_next_sibling("tr")

def move(driver):
    
    i=2
    count=1
    find()
    while (count<=9):
        elem=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents > div > div > a:nth-child(%d)"%i)
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        time.sleep(0.5) 
        i=i+1
        count+=1
        find()
    root=0
    while root<=2: #첫페이지를 제외한 넘기기 몇번할꺼인지 root<=1 3페이지 탐색
        driver.implicitly_wait(10) 
        time.sleep(0.5) 
        elem=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents > div > div > a.btnNext")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(10) 
        time.sleep(0.5) 
        i=4
        count=1
        find()
     
        while(count<=9):
            elem=driver.find_element_by_css_selector("#boxDayHistory > div > div.box_contents > div > div > a:nth-child(%d)"%i) #boxDayHistory > div > div.box_contents > div > div > a:nth-child(12) #종료지점
            elem.send_keys(Keys.RETURN)
            driver.implicitly_wait(10) 
            time.sleep(0.5) 
            i+=1
            count+=1
            find()
        root+=1
            
                
with open("종목명.txt","a",encoding="utf-8") as f:
    f.write("=====날짜,시가,고가,저가,종가====")       
    f.write("\n")         
        
move(driver)
