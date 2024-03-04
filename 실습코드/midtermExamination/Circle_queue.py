

class Queue(object):
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self,capacity) -> None:
        self.front=0
        self.rear=0
        self.no=0
        self.capacity=capacity
        self.queue=[None] *self.capacity
        
        #queue의 속성으로 enqueue->rear dequee->front no=elem_count 
        
    def is__full(self):
        return self.no>=self.capacity
    
    def is_empty(self):
        return self.no<=0
    
    def enqueue(self,data): #Enqueue의 방향 rear에서의 삽입
        if(self.is__full()):
            raise self.Empty
        self.queue[self.rear]=data
        self.rear+=1
        self.no+=1
        if self.rear>=self.capacity:
            self.rear=0
            
    def dequeue(self):
        if self.is_empty():
            raise self.Empty
        data=self.queue[self.front] #front방향에서 dequeue발생
        self.queue[self.front]=None
        self.front+=1
        self.no-=1
        if self.front>self.capacity:
            self.front=0 
        return data
     
    def peek(self): #dequeu방향 rear에서 데이타를 조회합니다
        if self.is_empty():
            raise self.Empty
        data=self.queue[self.rear]
        print("peek elem {}".format(data))
        return data
    
    def find_elem(self,key)->any:
        idx_buffer=list()
        if self.is_empty():
            raise self.Empty
        
        for i in range(self.no): #i의 방향을 front의 숫자로 재조정해야한다
            idx=(i+self.front)%self.capacity
            if self.queue[idx]==key:
                idx_buffer.append(idx)
                print("해당 key {}는 queue idx {}에 존재합니다".format(key,idx))
        
        return idx_buffer if len(idx_buffer)!=0 else False
    
    
    def clear(self):
        if self.is_empty():
            raise self.Empty
        
        #clear방향 FRONT->REAR FIFO구조
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            self.queue[idx]=None
        print("Clerar확인")
        
    def dump(self):
        #dump 방향 front->rear        
        if (self.is_empty()):
            raise self.Empty
        location=self.front
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            print("idx location{} key {} ".format(location,self.queue[idx]),end=" ")
        location=(location+i)%self.capacity
        if location>=self.capacity:
            location=0        
    def debug(self)->None:
        """front rear의 위치와 elem의상태를 확인합니다 """
        print("locationc check")
        print("front location {} rear location {} Elemnt_count {}".format(self.front,self.rear,
                self.no))
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
    q.debug()
    q.enqueue(6)
    q.find_elem(2)
    q.find_elem(5)
    q.enqueue(4)
    q.peek()
    # q.__contains__(3)
    q.debug()
    q.clear()
    
        
        
    
    
    
                      
        
    
    