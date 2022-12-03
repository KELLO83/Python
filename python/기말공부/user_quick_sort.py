import random
from typing import *
def sort (data:Sequence,left:int,right:int) -> None:
    pl=left
    pr=right
    pivoit = (pl+pr)//2
    
    while pl <= pr:
        while data[pl] < data[pivoit]:
            pl +=1 # 기준점보다 큰곳에어 중지한다
        while data[pr] > data[pivoit]:
            pr -=1 # 기준점보다 작은곳에서 중지한다
        if pl <= pr:
            data[pl], data[pr] = data[pr] , data[pl]
            pr-=1
            
            pl+=1
            
    if  pl < right:
        sort(data,pl,right)
    if  pr > left:
        sort(data,left,pr)
        
        
        
    

if __name__ == "__main__":
    data = [7,6,5,8,3,5,9,1,6]
    data = [ random.randrange(20)  for i in range(10)]
    print("정렬전",data)
    sort(data,0,len(data)-1)            
    print("정렬완료",data)    