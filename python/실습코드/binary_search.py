#이진 검색
#오름 차순이나 내림차순으로 일단 정렬되어있어야한다

from typing import *
def acsending_check(data,arr)-> bool: 
    """ 오름차순으로 사용자가 입력했는지 검사하는 function"""
    max=data
    for i in range(len(arr)):
        if arr[i]==None:
            return True
        if arr[i]>max:
            return False
    return True
def binary_seach(arr:Sequence,key:Any)->Any:
    """이진 검색 binary_serach"""
    
    start_arr=0
    last_arr=len(arr)-1 #전체길이에서 하나뺴줘야 실존하는 마지막 arr
    
    while True:
        middle_arr=(start_arr+last_arr)//2 #// 몫 연산자
        
        if arr[middle_arr]==key:
            return middle_arr
        elif arr[middle_arr]<key: # arr[i]가 key값보다 작다면 왼쪽버림
            start_arr=middle_arr+1 
        elif arr[middle_arr]>key:
            last_arr=middle_arr-1 
            
        if start_arr>last_arr:#왜 start_arr>=last_arr이면 안될까????
            """ 
            logic
            1 3 5 7 9일떄 3 key_find
            start=0 last=4 middle=2
            start=0 last=1 midldle=0
            start=1 last=1 middle=1 
            start==last 일경우 해당 배열의 원소가 사용자가 찾고자하는 원소일경우가있음
            """
            break
        
    return -1

if __name__=="__main__":
    elem=int(input("원소의 갯수를 입력하세요"))
    x=[None for _ in range(elem)]
    
    print("배열의 데이타를 오름차순으로 입력하세요!!!")
    for i in range(len(x)):
        x[i]=int(input(f"[{i}]번째에 넣을 원소를 입력하세요"))
        sort_check=acsending_check(x[i],x)
        if sort_check==False:
            print("오름차순으로 입력해주세요")
            exit()
    find_user_key=int(input("검색할 값을 입력하세요"))
    
    res=binary_seach(x,find_user_key)
    
    if res==-1:
        print("검색값을 갖는 원소가 존재하지 않습니다")
    else:
        print(f"해당 검색값 {find_user_key}는 arr의 {res}번쨰 위치에 존재합니다")