# 선형 검색 알고리즘을 보초법으로 탐색을 해보자
# 보초법은 내가 찾고자하는 key값을 배열의끝에 해당 ket값을 추가하여 시간을 줄일수있디
from typing import *

import copy
'''
copy.copy(x)
x의 얕은 사본을 반환합니다.= >새로운 객체가 아닌 메모리만 원래있던 객체를 지칭

copy.deepcopy(x[, memo])
x의 깊은 사본을 반환합니다.=> 새로운객체
'''


def search(arr:Sequence,key:Any)->Any:
    copy_arr=copy.deepcopy(arr)
    copy_arr.append(key)#보초법 사용자가 찾고자하는 key 값을 맨끝에 추가한다
    i=0
    
    while True:
        if copy_arr[i]==key:
            break
        i+=1
    
    return -1 if i==len(arr) else i #??????????? 
        
    
    #copy_arr[i]가 len(arr) 일경우 검색실패
    """
    if(int(integer_str_value) > 0):
            return True
        else:
            return False
    """
    """
    return True if int(integer_str_value) > 0 else False
    """
    # return if else를 한줄로 합칠수있다
    
    
    
    
    
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
        