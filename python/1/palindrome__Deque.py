import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect

class Unit():
    def __init__(self,name):
        self.name=name
        
    
def inPalindrome(self,s:str)->bool:
    strs:collections.deque=collections.deque() #strs를 담는 데이터형 박스
    #import collections.deque 데크 양방향에서의 데이터 삽입과 삭제
    
    for char in s:
        if char.isalnum(): #isalnum 문자열이 알파벳[a-z,A-Z] 숫자[0-9]로 구성되어있는지 확인
            strs.append(char.lower())
            #char.lower 대문자를 소문자로 바꾸기
    
    while len(strs)>1:
        if strs.popleft()!=strs.pop(): #popleft deque에서 지원하는 왼쪽에서 데이터 pop
            return False   
        
    return True    

a=Unit("test")

value=inPalindrome(a,"Ko1221OK")

if value==True:
    print("True")
else:
    print("False")
    




