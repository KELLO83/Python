
import collections
import heapq
import functools
import itertools
import re
import sys
import math



strs=input("input strs ")

def check(strs)->True:
    stroge=list()
    count=0
    
    for str in strs:
        stroge.append(str)
        count=count+1
        
        
    for check in stroge:
        print(type(check))
        if check.isalnum()==False:
            print("{} 숫자나 영문자가 아니다".format(check))
    
    while(True):
        if stroge.pop(0)!=stroge.pop():
            return False
        else:
            return True
value=check(strs)


