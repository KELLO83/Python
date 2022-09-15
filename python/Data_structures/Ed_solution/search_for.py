#선형검색을 while이 아닌 for문으로 해보자

from typing import *

def search(a,key)->Any:
    for i in range(len(a)): # while이 아닌 for문으로 실행하엿다 
        if a[i]==key:
            return i
    return -1


if __name__=="__main__":
    num=int(input("원소의 수를 입력하세여"))
    x=list()
    x=[None for _ in range(num)]
    for i in range(len(x)):
        x[i]=int(input("x[{}]번째에 넣을 원소를 입력히세여".format(i)))
    user_key=int(input("사용자가 찾고자하는 key값을 입력해주세요"))
    
    res=search(x,user_key)
    
    if (res==-1):
        print("검색값을 찾는 원소를 가지고있지 않습니다")
    else:
        print(f"겁색이 성공하였습니다 해당원소는 배열의 {res}번째에 존재합니다")
        