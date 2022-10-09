#배열 원솔르 역순으로 정렬하는 프로그램

from typing import Any,MutableSequence



def reverse_arr(list_:MutableSequence):
    le=len(list_)
    
    for i in range(le//2):
        list_[i],list_[le-i-1]=list_[le-i-1],list_[i] #역순으로 정렬하는swap 중요
        


if __name__=="__main__":
    print("배열의 원소를 역순으로 정렬합니다")
    nx=int(input("원소수를 입력하세요"))
    list_=[None]* nx
    for i in range(nx):
        list_[i]=int(input(f"{i}번째 배열의 원소를 입력하세요"))
    
    reverse_arr(list_)
    
    print("reverse finish")
    print(list_)