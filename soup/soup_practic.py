import requests
from bs4 import BeautifulSoup

res=requests.request('GET',"https://comic.naver.com/webtoon/weekday")


soup=BeautifulSoup(res.text,"lxml") #html 정보로 soup객체가 저장한다

print(soup)# 페이지의 html모든 정보 출력

print(soup.title) #페이지의 title 태그 출력

print(soup.title.get_text()) #title 태그를 text로 변환하여 출력한다

print(soup.a) # 첫번쨰로 발견되는 a태그 출력

print(soup.a.get_text()) #a태그의 text로 출력 

print(soup.a.attrs) #첫번쨰로 발견되는 a태그를 딕셔너리 형태로 반환한다

print(soup.a["onclick"]) #oneclick 에 해당하는 key값을 출력한다 soup.a.attrs 의 키값

print("-------------")


result=soup.find("div",attrs={"class":"end_page"})
print(result)

with open("test.htm","w",encoding="utf8") as ef:  #
    ef.write(result.text)  
    
            
print("---------") 
                     

rank_1=soup.find("li",attrs={"class":"rank01"})

print("rank_1의 html  정보를 출력합니다")
print(rank_1)

print("------------")

print(rank_1.get_text())

print("------------")

print(rank_1.img.attrs) #rank_1 에서 img 태그안에정보를 딕셔너리 혈태로 반환한다

print("src 의 value 값")
print(rank_1.img["src"]) #rank_1에서 img태그정보안에서 src의 value값을 반환한다 


rank2=rank_1.next_sibling.next_sibling #rank 1다음의 형제 태그

print("rank2 \n",rank2) 

print("딕셔너리 형태",rank2.a.attrs) #rank2 의 처음발견되는 a태그의 정보를 딕셔너리 형태로 반환한다

print("a[href] value",rank2.a["href"]) #rank2 의 처음발견되는 a태그중에서 속성이 href 의 value 값을 return한다


rank3=rank2.find_next_sibling("li") #rank2다음으로 나오는 li태그를 rank3 객체에 저장한다

print("rank3\n",rank3) #rank3의 html정보를 저장한다 

print("rank3.img태그\n",rank3.img) #rank3의 img태그만 저장한다

print("""rank3.img["title"]\n""",rank3.img["title"]) #rank3 의 img태그안에서 title의 value값을 return한다


all_search=rank3.find_next_siblings("li")

for i in all_search: #정상작동
    print("------------")
    print(i)
    print("get_text()실행\n",i.get_text())
    temp=i.img["src"]
    print("""i.img["src"]""",temp) 
    
    
    
    
# print("all_search.img\n\n",all_search.a.get_text())

# for i in all_search.img:
#     print(i)
    
    

