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
        pass
    class Full(Exception):
        pass

class Queue(object):
    def __init__(self,capaicty=5) -> None: #속성 front  rear count capaicty
        self.front=0
        self.rear=0
        self.count=0
        self.capaicty=capaicty
        self.queue=[None] *capaicty
        
    def __contains__(self,value):
        return self.count__(value)
    
    def __len__(self): #queue count elemnt
        return self.count
                
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
        if(self.is_full()):
            raise Err.Empty
        self.count+=1
        self.queue[self.rear]=value #데이터 삽입완료
        self.rear+=1 #rear의 위치를 조정합니다
        if self.rear>=self.capaicty: #서클큐 
            self.rear=0 #0번지로 이동합니다
        
    def dequeue(self): # front에서 하나꺼냅니다
        if(self.is_empty()):
            raise Err.Empty   
        self.count-=1
        data=self.queue[self.front]
        self.front+=1
        if(self.front>=self.capaicty): #서클큐 위치 재조정
            self.front=0 
        return data       
    
    def peek(self): #front에서 데이터를 peek합니다
        if(self.is_empty()):
            raise Err.Empty
        data=self.queue[self.front]
        print("location {} peek {} ".format(self.front,data))
        return data
    def find_elem(self,value): #queue에서 value값을 찾으면 1 없으면 -1반환
        for i in range(self.count): #find 시작 front위치에서 시작
            index=(self.front+i)%self.capaicty #원형큐로써 나누기 구현
            if(self.queue[index]==value):
                print("해당 value {} 를 가진 index는 {}번쨰에 위치합니다".format(value,index))
                return index #해당 value값이 들어있는 index번호를 리턴합니다
            
        return False #Findn false
    
    def count__(self,value): #큐에있는 동일 원소를 카운트하여 반환합니다
        elem_count=0
        for i in range(self.count):
            index=(self.front+i)%self.capaicty
            if self.queue[index]==value:
                elem_count+=1
        print("해당 원소 {} 를 Queue에 {}개 가지고있습니다".format(value,elem_count))
        return elem_count
    def clear(self): #queue clear
        for i in range(self.count):
            self.queue[(self.front+i)%self.capaicty]=None
        print("")
        print("clear확인")
        print(self.dump())
        print("clear확인")
        
    def dump(self): # 출력방향 front->rear
        if(self.is_empty()):
            raise Err.Empty
        location=self.front
        for i in range(self.count):
            print("{}번쨰 index 원소 {}".format(location,self.queue[(self.front+i)%self.capaicty]))
            location+=1
            if location>=self.capaicty:
                location=0
            
    def debug(self)->None:
        """front rear의 위치와 elem의상태를 확인합니다 """
        print("locationc check")
        print("front location {} rear location {} Elemnt_count {}".format(self.front,self.rear,
                self.count))
        print("")
        print("DEBUG")
        self.dump()
        print("DEBUG")
        print("")
        



if __name__=="__main__":
    q=Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(6)
    q.find_elem(2)
    q.find_elem(5)
    q.enqueue(4)
    q.peek()
    q.__contains__(3)
    q.count__(4)
    q.debug()
    q.clear()
    
    

    
        
            


        
             