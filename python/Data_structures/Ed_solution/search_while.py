# 배열에서 선형 검색 알고리즘을 이용한 key 값 find

from typing import *
def sequence_search(a:Sequence,key:Any)->Any:
    """ arr에서 해당하는key값을 찾아 반환하는 함수"""
    #while 문을 통한 key값 find
    i=0
    while True:
        if i==len(a):#만약 배열이 3칸이라면 len(a)=3이다 그런데 arr[2]까지만 존해므로 arr[3]이 되는순간 out of range이므로 검색을 종료한다
            return -1,-1 # i의 값과 시퀀스 a의 길이가 같아지는경우 해당배열에는 해당 ket값이 없으므로 false return    
        if a[i]==key:#어떤 arr이 해당 key값과 일치하는 elem이 있다면 그 해당하는 배열의 elem을 return 한다
            return a[i],i
        else:
            i+=1

if __name__=="__main__":
    num=int(input("원소의 수를 입력하세여"))
    x=list()
    x=[None for _ in range(num)]
    for i in range(len(x)):
        x[i]=int(input("x[{}]번째에 넣을 원소를 입력히세여".format(i)))
    user_key=int(input("사용자가 찾고자하는 key값을 입력해주세요"))
    
    
    res,res_count=sequence_search(x,user_key)
    
    if res==-1:
        print("검색값을 찾는 원소를 가지고 있지 않습니다")
    else:
        print("검색값은{}입니다 검색으로 찾고자하는 배열의 위치는 {}입니다".format(res,res_count))