import requests
from bs4 import BeautifulSoup


url="https://news.daum.net/"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/97.0.4692.71 Safari/537.36"}

res=requests.get(url,headers=headers)

if res.status_code==requests.codes.ok:
    print("정상")
else:
    print(f"문제 발생 에러코드{res.status_code}")
    

soup=BeautifulSoup(res.text,"lxml")
with open("check.htm","w",encoding="utf-8") as file:
    file.write(str(soup))
    

# list=soup.find_all("strong",attrs={"class":"tit_thumb"})
list=soup.find_all("strong",class_="tit_thumb") 

list_1=soup.find_all("strong")

with open("strong_all_tag.htm","w",encoding="utf-8") as p:
          p.write(str(list_1))

print("list\n",list)

with open("strong_tag.htm","w",encoding="utf-8") as f:
    f.write(str(list))
    
print("----------")

for i in list:
    
    print(i.get_text())
    
    
kello=soup.find("strong",class_="tit_thumb")

print("test\n",kello)
    
print("test_2\n",kello.contents) #.contents 는 stong태그의 하위 태그 <a>태그의 내용을 리스트형태로 출력한다



for i in kello:
    print("for문",i.string) #get_text()와 작동법이 비슷하지만 strign은 화이트스페이스도 가져온다 
    #그래서 'n' 도 문자열로 인식하기때문에 for문을 사용해야한다 다만 화이트스페이스나 다른 
    #특이 문자열이 없을 경우 for문을 사용을 안해도된다 



print("paraent",kello.parent) #strong태그를 감싸고 있는 상위태그 div class="cont_thumb"출력

print("pareant의paraent\n",kello.parent.parent) #div class="cont_thumb" 를담고있는 상위태그 출력

print("##############")

print(kello.parent.name) #.name객체가 처음으로 가지고있는 태그를 반환한다 

result=kello.find_parent("div") #kello.parent 와 작동밥법 같다

print("result",result)

link=kello

print("$$$$$$$$$$$$")

for parent in link.parents: #strong 태그에서 상위태그가없을때까지 모든 태그들의 .name출력한다 순회하기
    print(parent.name)
else:
    print(parent.name)
    
t1=soup.select("#cSub > div > ul") # css selector를 이용하여 검색 csub라는 div id="csub"를 찾은후
#하위태그 div참조후 그 하위태그 ul 태그를 참조한다 ul class="list_issue" 참조할수있다

print("t1",t1)

print(type(t1))

print("------------------")

for i in t1: ###########?? 어려움 t1.find_all("storng",class_"tit_thumb) 작동안되는이유? 2중for문
    tag=i.find_all("strong",class_="tit_thumb") #find_all 해당모든태그를 리스트형태로 가져온다
    for i in tag:
        print(i.get_text())
        
    
v1=soup.find("div",{"id":"cSub"})

v2=v1.select_one("#cSub > div > ul ") #select_one 은 list 형태로 반환하지않는다 



v3=v2.find_all("a",class_="link_txt")


print(v3)
print("##########")

for i in v3:
    print(i.get_text())
    

print("인덱싱",v3[:3]) #find_all 은 list형태로 반환하기때문에 find_next_siblings 을 사용할수없다
#안덱싱을 사용하여 세부참조해야됨

v4=v3[:3]

print("@@@@@@")

for i in v4:
    print(i.get_text())
    # print(i.string)

p1=soup.find("ul",class_="list_headline")







