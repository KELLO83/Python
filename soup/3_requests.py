import requests

res=requests.get("http://www.google.com")
# res=requests.get("http://nadiciding.tistory.com")
print("응답코드:",res.status_code)#200이면 정상 404 비정상


if res.status_code==requests.codes.ok:
    print("정상")
else:
    print(f"문제 발생 에러코드{res.status_code}")
    

res.raise_for_status()#정상 실행안될시 오류를 내고 강제종료시킴
print("웹 스크래핑을 진행합니다")


print(len(res.text))
print(res.text)


with open("mygoogle.htm","w",encoding="utf8") as ef: #with문 사용시 close 불필요
    ef.write(res.text)