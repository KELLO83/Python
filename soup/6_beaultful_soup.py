import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)

res.raise_for_status()  #url 열기 실패시 강제종료


soup=BeautifulSoup(res.text,"lxml") # html문서값을 lxml 파서를 통해 soup객체에 저장한다 
# print(soup)


# print(soup.title) 

# print(soup.title.get_text())

# print(soup.a) #첫번쨰로 발견되는 a태그

# print(soup.a.attrs) #a 속성정보를 반환해주고 딕셔너라형태로 반환

# print(soup.a["href"]) # a 속성의 href 속성값을 반환해준다

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) #처음으로발견되는 a태그중에서 class 가 Nbtn_upload인 속성정보를 가져온다

# print(soup.find(attrs={"class":"Nbtn_upload"})) #class 속성이  Nbtn_upload 인 원소를 찾아줘


# print("------")


rank1=soup.find("li",attrs={"class":"rank01"})

# print(rank1.a.get_text())
rank2=(rank1.next_sibling.next_sibling)

rank3=(rank2.next_sibling.next_sibling)


rank2=rank3.previous_sibling.previous_sibling
# print(rank2)


temp=rank1.find_next_sibling("li")
print(temp)

temp1=rank2.find_next_sibling("li")
print(temp1.a.get_text())

temp2=rank2.find_previous_sibling("li")
print(temp2.a.get_text())


all=rank1.find_next_siblings("li")

print("------------------")

print(all)










