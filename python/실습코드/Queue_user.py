from typing import Any 
"""
typing.Any
제한되지 않는 형을 나타내는 특수형.
모든 형은 Any와 호환됩니다.
Any는 모든 형과 호환됩니다.
"""
#circled queue 
#기본 FIFO 구조 Front=>dequeue rear=>enqueue 

class Err(Exception):
    class Empty(Exception):
        print("Queue is empty")
        pass
    class Full(Exception):
        print("Queue is FULL")
        pass

class Queue(object):
    def __init__(self,capaicty=5) -> None: #속성 front  rear count capaicty
        self.front=0
        self.rear=0
        self.count=0
        self.capaicty=capaicty
        self.queue=[None] *capaicty
        
    def __contains__(self,value):
        return self.count(value)
    
    def is_full(self):
        if(self.count>=self.capaicty): #원소의 갯수가 count가 capaicty보다 클떄?
            return True
        return False
    # is full 상태라면 true를 return 아니라면 false를 return 합니다        
    
    def is_empty(self):
        if(self.count<=0): #원소의갯수가 0보다 작으면 empty
            return True
        return False
    # is empty 상태라면  elem의 상태가 0보다 작거나 같습니다 
    def enqueue(self,value): #데이터를 큐에 삽입합니다 
        if(self.is_full):
            raise Err.Full
        self.count+=1
        self.queue[self.rear]=value #데이터 삽입완료
        self.rear+=1 #rear의 위치를 조정합니다
        if self.rear>=self.capaicty: #서클큐 
            self.rear=0 #0번지로 이동합니다
        
    def dequeue(self): # front에서 하나꺼냅니다
        if(self.is_empty):
            raise Err.Empty   
        self.count-=1
        data=self.queue[self.front]
        self.front+=1
        if(self.front>=self.capaicty): #서클큐 위치 재조정
            self.front=0 
        return data       
    
    def peek(self): #front에서 데이터를 peek합니다
        if(self.is_empty):
            raise Err.Empty
        data=self.queue[self.front]
        return data
    def find(self,value): #queue에서 value값을 찾으면 1 없으면 -1반환
        for i in range(self.count): #find 시작 front위치에서 시작
            index=(self.front+i)%self.capaicty #원형큐로써 나누기 구현
            if(self.queue[index]==value):
                return index #해당 value값이 들어있는 index번호를 리턴합니다
            
        return False #Findn false
    
    def count(self,value): #큐에있는 동일 원소를 카운트하여 반환합니다
        elem_count=0
        for i in range(self.count):
            index=(self.front+i)%self.capaicty
            if self.queue[index]==value:
                elem_count+=1
        return elem_count
    def clear(self): #queue clear
        for i in range(self.count):
            self.queue[(self.front+i)%self.capaicty]=None
        print("clear확인")
        print(self.dump)
        print("clear확인")
        
    def dump(self):
        if(self.is_empty):
            raise Err.Empty
        location=self.front
        for i in range(self.count):
            data=self.queue[(self.front+i)%self.capaicty]
            print("{}번째 index value {}".format(location,data))
            location=(location+i)%self.capaicty
            
            
            


if __name__=="__main__":
        pass
    
        
            


        
             