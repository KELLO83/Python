import requests
from bs4 import BeautifulSoup


url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)


res.raise_for_status()  #url 열기 실패시 강제종료
soup=BeautifulSoup(res.text,"lxml")


cartoos=soup.find_all("a",attrs={"class":"title"}) #a태그중 class 속성이 title인 모든 요소를 가져온다
""" 
<a href="/webtoon/list?titleId=758037&amp;weekday=mon" 
onclick="nclk_v2(event,'thm*m.tit','','2')" class="title" title="참교육">참교육</a>
""" #a태그안에 class="title" 인 모든 요소들을 가져온다
#class 속성이  title인 모든 'a' element 반환

for i in cartoos:
    print(i.get_text())# utf8로된 문자만 가져와서 출력을 한다
    
    
res=requests.get("https://comic.naver.com/webtoon/list?titleId=783053&weekday=tue")

res.raise_for_status()   

soup=BeautifulSoup(res.text,'lxml')

tag=soup.img #soup 객체에 img라는속성을  tag에 저장한다
print(type(tag)) #tag 의  type을 반환한다


    
search=soup.find_all("td",attrs={"class":"title"}) #td태그중에서 class 가 title인 모든 정보를 가져온다


def assemble(search):
    for i in search:
        temp1=i.get_text()
        temp2=i.a["href"]
        print(temp1+"https://comic.naver.com"+temp2)

def average(number):
    global count
    global total
    count=0
    total=0
    for i in number:
        count=count+1
        
        result=i.find("strong").get_text()
        total=float(result)+total
        print(total)
        
    result=total/count
    print("평균 평점은",result)
    return result    
        

        
class Ass():
    total=0
    def __init__ (self,name):
        self.name=name
    
    def assemble(self,search):
        for i in search:
            temp1=i.get_text()
            temp2=i.a["href"]
            print(temp1+"https://comic.naver.com"+temp2)
    def average(self,number):
        global count
        count=0
        for i in number:
            count+=1
            temp=i.find("strong").get_text()
            self.total=self.total+float(temp)
            
        self.total=self.total/count
        
            

for i in search:
    print(i.get_text())
    

for i in search:
    result=i.a["href"] #a태그의  href value값을 리턴한다
    print("https://comic.naver.com"+result)
    

print("-------------")

assemble(search)

a1=Ass("kello")

a1.assemble(search)


number=soup.find_all("div",attrs={"class":"rating_type"})



for i in number:
    print("------")
    print(i)
    temp=i.find("strong")
    print(temp)
    print(temp.get_text())
    
    
    
print("---------")


average=average(number)

result=a1.average(number)

print("a1.total",a1.total)





    