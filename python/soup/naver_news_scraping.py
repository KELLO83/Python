import requests
from bs4 import BeautifulSoup


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/97.0.4692.71 Safari/537.36"}

url="https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100"

res=requests.get(url,headers=headers)


if res.status_code==requests.codes.ok:
    print("정상")
else:
    print(f"문제 발생 에러코드{res.status_code}")
    

soup=BeautifulSoup(res.text,"lxml")

print(soup.prettify) #html 문서를 soup.prettify를 이용하면 깔끔하게 보여준다


research=soup.find("div",class_="cluster_group _cluster_content")

print("div태그\n",research.prettify,end="\n research finsih")

temp=research.div.attrs["class"] # class_"cluster_group _cluster_content" 중에서 처음으로발견되는 div태그로 시작하는 class의 value 값을 리턴한다 
#div.attrs["속성"] 은 해당 줄만 가져오고 하위태그들의 정보는 가져오지않는다

print("test\n\n",temp,end="\ntest")

"""
#resarch의 첫줄부터 일부부분 가져온것
<div class="cluster_group _cluster_content">
<div class="cluster_body"> #처음으로 발견되는 div태그중 class_="cluster_body 이다 
<ul class="cluster_list">
<li class="cluster_item">
<div class="cluster_thumb">
<div class="cluster_thumb_inner">
<a class="cluster_thumb_link nclicks(cls_pol.clsart)" href="https://news.naver.com/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=100&amp;oid=011&amp;aid=0004013590">
<img alt="" height="90" onerror="javascript:this.src='https://ssl.pstatic.net/static.news/image/news/2009/noimage_132x90.png';this.style.width=132;this.style.height=90;" src="https://imgnews.pstatic.net/image/origin/011/2022/01/28/4013590.jpg?type=ofullfill132_90" width="132"/>
"""

search=soup.find("div",attrs={"class":"cluster_group _cluster_content"})

print("\n\nsearch\n",search,end="\n완료")
"""
<div class="cluster_group _cluster_content">
<div class="cluster_body">
<ul class="cluster_list">
<li class="cluster_item">
<div class="cluster_thumb">
<div class="cluster_thumb_inner">
<a class="cluster_thumb_link nclicks(cls_pol.clsart)" href="https://news.naver.com/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=100&amp;oid=016&amp;aid=0001944358">
<img alt="" height="90" onerror="javascript:this.src='https://ssl.pstatic.net/static.news/image/news/2009/noimage_132x90.png';this.style.width=132;this.style.height=90;" src="https://imgnews.pstatic.net/image/origin/016/2022/01/28/1944358.jpg?type=ofullfill132_90" width="132"/>
</a>
"""

result=search.div.attrs["class"] #처음으로 발견되는 div태그중 속성이 class인값의 key값을 return한다 단 자기자신은 제외한 제일 첫번쨰 발견태그

print("result=",result,end="\n")


list=search.find_all("li") #헤드라인 뉴스를 가져온다 4개 네이버뉴스는 항상 최신화되서 계속 바뀜

print("list\n\n\n",list,end="\n완료")


for lists in list: #find_all 은 list의 형태로 가져오기때문에 for문을 활용하여 .get_text()를 사용하여 글씨만 가져온다
    print(lists.get_text())
    

# important1=soup.find("ul",class_="section_list_ranking_press _rankingList")
#important1=soup.find("ul",attrs={"class":"section_list_ranking_press _rankingList")
                     
# important2=soup.find("ul",attrs={"id":"_rankingList5"})
important=soup.find("ul",id="_rankingList0") #????

# 태그, 키이름=값
# 태그, 키이름={키이름 : 값, 키이름2 :  값2}


final=important.find(class_="list_tit nclicks('rig.renws2')")

print(final.prettify,end="final.prettify\n\n")

k1=important.find("li")


# t2=final.find_next_sibling("li")  #비작동 find_next_sibling을 사용하기위해서는 같은 트리안에 있어야한다  
"""
<ul class="section_list_ranking_press _rankingList" id="_rankingList0" style="display: block">
    <li>..<li> # find_next_sibling("li") 로 지칭한다 이후 find_next_sibling을 통해 그다음 <li> 태그를 지칭할수있다
    <li>..<li>
    <li>..<li>
    <li>..<li>                                                
"""


all_check=k1.find_next_siblings("li")

count=1

for i in all_check:
    (i.get_text()).replace(" ","")
    print(i.get_text())
    
    count+=count
    
    
    