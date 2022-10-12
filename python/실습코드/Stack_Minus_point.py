from typing import *


class Fixedstack():
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.stk=[None for _ in range(self.capacity)]
        self.ptr=-1 #스택포인터를 init -1로 잡는다 
        #처음 원소가 삽입된후에는 스택포인터가 0이고 스택 arr[0] 번지에 데이터가 찬다
    def __len__(self):
        return self.capacity
    
    def is_empty(self):
        return self.capacity<=-1
    
    def is_full(self): #만약 stk capacity 5 init arr[5] 번지 삽입완료시 stk.ptr는 5번지이다
        return self.ptr>self.capacity
    
    def push(self,data):
        if (self.is_full()):
            raise self.Full

        
        self.stk[self.ptr+1]=data #arr[stk] 랑 ptr stk의 번호가 같으므로 그다음idx에다가 push하기위해서는 ptr을 1증가시킨곳에 psuh를 해야한다
        self.ptr+=1
        
    def pop(self):
        if (self.is_empty()):
            raise self.Full
        
        data=self.stk[self.ptr] #stk상단부분을 포인터가 바로 잡고있다 그곳의data를 바로 return을한다
        self.ptr-=1 #point위치를 한개줄인다
        return data
    def peek(self):
        if self.is_empty():
            raise self.Empty
        
        data=self.stk[self.ptr]
        return data
    
    def clear(self): #stk __init__ clear
        print("clear stack")
        for i in range(self.ptr):
            self.stk[i]=None
        self.ptr=-1
        print("clear stack")
        
    def count(self,data):
        count=0
        for i in range(self.ptr,-1,-1):
            if self.stk[i]==data:
                count+=1
        print("stk in elem{} count{} ".format(data,count))
        
        return count
    
    def find_location(self,data): 
        #스택에 존재하는 key값의 stk index번호를 전부 찾는다
        stk_buffer=list()
        
        if self.is_empty():
            raise self.Empty
        for i in range(self.ptr,-1,-1): #검색순서 상단부터 꼭대기
            if self.stk[i]==data:
                stk_buffer.append(i)
        print("find location value {} buffer {}".format(data,stk_buffer))
        return stk_buffer
    
    def dump(self):
        if (self.is_empty()):
            raise self.Empty
    # 스택은 FILO구조입니다
        for i in range(self.ptr,-1,-1):
            print("{}".format(self.stk[i]),end=" ")
        
        print()
    def stack_status(self):
        print("현재 스택의 갯수는 {}입니다".format(self.ptr+1))
        
        
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

        
        
         
                
                
                
        
