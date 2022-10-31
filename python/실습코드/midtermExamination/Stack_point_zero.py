#stk point init zero 

from typing import Any


class Fixedstack():
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self,capacity) -> None:
        self.capacity=capacity    
        self.stk=[None]*self.capacity
        self.ptr=0 #스택포인트를 0으로 잡는다
    #원소를 한개 삽입완료할시 stk[0]번지에 원소가 차면서 stk.ptr=1번지이다
    #즉 point가 한단계 앞서간다
        
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
        return True
    
    def pop(self):
        if self.is_empty():
            raise self.Empty
        
        data=self.stk[self.ptr-1]
        self.ptr-=1
        return data
    
    def peek(self):
        if self.is_empty():
            raise self.Empty
        
        data=self.stk[self.ptr-1]
        return data
    
    def clear(self):
        if self.is_empty():
            raise self.Empty ("stack is empty")
        
        for i in range(self.ptr-1,-1,-1):
            self.stk[i]=None
            
        self.ptr=0
            
        print("clear확인")
        
    def find_location(self,data):
        stk_buffer=list()
        if self.is_empty():
            raise self.Empty
        
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i]==data:
                stk_buffer.append(data)
                
    def dump(self):
        if self.is_empty():
            raise self.Empty
        
        for i in range(self.ptr-1,-1,-1):
          print("{}".format(self.stk[i]),end=" ")
        
        print()
    def stack_status(self):
        print("현재 스택의 갯수는 {}입니다".format(self.ptr))
    
    def count(self,data):
        count=0
        if self.is_empty():
            raise self.Empty
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i]==data:
                count+=1
                
        return count        
if __name__=="__main__":
    stack=Fixedstack(10)  
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    stack.dump()
    stack.pop()
    stack.dump()
    stack.peek()
    stack.count(4)
    stack.find_location(4)
    stack.stack_status()
    stack.dump()
    stack.clear()
    stack.stack_status()

        
        