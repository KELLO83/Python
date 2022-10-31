#recur()은 자기자신을 2번호출한다
from typing import *
def recur(n):
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)
        
def recur_2(n):
    while n>0:
        recur(n-1)
        print(n)
        n=n-2

if __name__=="__main__":
    recur(4)