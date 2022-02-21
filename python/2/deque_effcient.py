#queue effcient memory
#FIFO
#First in first out

class Queue():
    def __init__(self,name):
        self.name=name
        self.in_stack=[]
        self.out_stack=[]
     
    def _transfer(self): #메모비 비효율을 줄이기위한 변환
        while self.in_stack:# empty list는 False를 empty가 아닌 list는 True
            self.out_stack.append(self.in_stack.pop())
            
    def enqeue(self,itmes)->None:
        self.in_stack.append(itmes)
        print("enque {}".format(itmes))
    
    def deque(self)->None:
        if not self.out_stack:
                self._transfer()
        if self.out_stack:
            value=self.out_stack.pop()
            print("deque {}".format(value))
        else:
            print("Queue is empty")
            
    def peek(self)->None:
        value=self.in_stack[0] 
        print("peek {}".format(value))
    
    def check_queue_size(self)->None:
        print("check_queue size {}".format(len(self.in_stack)))
        
    
if __name__=="__main__":
    a=Queue('test')

    a.enqeue(1)
    a.enqeue(2)
    a.deque()
    a.enqeue(2)
    a.peek()

    a.enqeue(3)
    a.check_queue_size()

