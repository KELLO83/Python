#stk point init zero 

from typing import Any


class Fixedstack():
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self,capacity) -> None:
        self.stk=[None]*self.capacity
        self.capacity=capacity
        self.ptr=0 #스택포인트를 0으로 잡는다
        
    def __len__(self): #스택에 쌓여있는 데이터의 갯수를 알아내자
        return self.ptr
    
    def is_empty(self):
        return self.ptr<=0
    
    def is_full(self):
        return self.ptr>=self.capacity
    
    def push(self,data):
        if self.is_full():
            raise self.Full
        self.stk[self.ptr]=data
        self.ptr+=1
        
    def pop(self):
        if self.is_empty():
            raise self.Empty
        data=self.stk[self.ptr]
        return data