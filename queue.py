#queue
#firs in first out
#FIFO

class Queue():
    def __init__(self,name)->None:
        self.name=name
        self.itmes=[]
        self.Queue_count=0 #큐의 현재 사이즈
           
    def Queue_is_empty(self)->bool:
        if len(self.itmes)==0:
            print("Queue is empty")
            
        else:
            print("Queue is not empty")
            
  
    def enqueue(self,push)->None:
        self.itmes.append(push)
        print("list append {}".format(push))
        self.Queue_count+=1
        
    def dequeue(self)->None:
        temp=self.itmes.pop(0)
        print("list pop {}".format(temp))
        self.Queue_count-=1
        
    def check_Queue_size(self)->None:
        count=len(self.itmes)
        print("check Queue size {}".format(count))
    
    def peek(self)->None:
        pk=self.itmes[0]
        print("Queue peek {}".format(pk))
        
a=Queue("test")

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)    

a.dequeue()        
a.peek()
a.check_Queue_size()
a.dequeue()
a.check_Queue_size()

if __name__=="__main":
    print("내부 실행")
    