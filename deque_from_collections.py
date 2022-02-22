#collection을 이용한 deque구현
import collections
from ctypes.wintypes import PUSHORT
from tabnanny import check
#queue First in First out

class queue():
    def __init__ (self,name):
        self.name=name
        self.itmes=collections.deque()
        self.queue_count=0 #큐의 사이즈
        
    def enqueue(self,data):
        self.itmes.append(data)
        print("enqueue {}".format(data))
        self.queue_count+=1
        
    def dequeu(self):
        value=self.itmes.popleft()
        print("deque {}".format(value))
        self.queue_count-=1
        
    def check_deque_size(self):
        check=len(self.itmes)
        print("check_stack_size {}".format(check))
        
    def peek(self):
        try:
            return self.itmes[0]
        except:
            print("queue is empty")
    def top(self):
        top=self.itmes[self.queue_count-1]
        print("queue top {}".format(top))
        
    def clear(self):    
        self.itmes.clear()
        return True
    
    def find(self,data):
        for i in self.itmes:
            if i==data:
                return True
        
        return False
    
    def deque_count(self,data): #data와 같은 요소의 개수를 측정한다
        count_elem=0
        for i in self.itmes:
            if i==data:
                count_elem+=1
        
        return count_elem
    
    def extend_deque(self,data_list): #데크의 오른쪽에 붙인다
        self.itmes.extend(data_list)
        print("extend_deque {}".format(self.itmes))
    
    def extend_left_deque(self,data_list):#데크의 왼쪽에 데이터를 붙인다    
        self.itmes.extendleft(data_list)
        print("exted_deque from left {} ".format(self.itmes))
        

                        
if __name__=="__main__":
    print("내부 모듈 실행")
      
    a=queue("test")

  
    
    
        
    
        
