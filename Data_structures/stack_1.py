#stack 
#Last in first out
#LIFO


from itertools import count
from pickle import FALSE


class Stack():
    def __init__(self,name,count) -> None:
        self.name=name
        self.itmes=list(0 for i in range(0,count)) #count 크기만큼 라스트 크기를 할당한다  list 요소가 0으로 전부 초기화되면서 10칸을 할당한다 
        self.stack_count=0 #스택의 현재 크기만큼 게속 변화한다
        self.stack_size=count #바뀌지않는 고유값
        print(type(self.itmes))
                                             
    def stack_is_empty(self) ->bool:
        
        if len(self.itmes)==0:
            print("stack is empty") 
        else:
            print("stack is not empty")
            
    def stack_is_full(self)->bool:
        if self.stack_count==self.stack_size:
            print("stack is full")
        else:
            print("stack is not full")
            
    def push(self,push)->None:
        try:
            self.itmes[self.stack_count]=push
        except:
            self.itmes.insert(self.stack_count,push)
        self.stack_count+=1
        print("stack is push {}".format(push))
    
    def pop(self)->None:
        try:
            temp=self.itmes.pop(self.stack_count-1)
            self.stack_count-=1    
            print("stack is pop from {}".format(temp))
        except:
            self.stack_is_empty()
    def check_stack_size(self)->None: 
        count=len(self.itmes)
        print("check stack size {}".format(count))
        
    def peek(self)->None:
        count=len(self.itmes)
        print("stack peek {}".format(self.itmes[count-1]))
        
    def ground(self)->None:
        print("stack ground {}".format(self.itmes[0]))
        
    def clear(self)->None:
        while(len(self.itmes)):
            self.itmes.pop()
        
        print("empty list{}".format(self.itmes))    
        
    def find(self,str)->True:
        for i in self.itmes:
            if i==str:
                return True
            else:
                return  False
    def dump(self)->list:
        value=list()
        for i in self.itmes:
            value.append(i)
        return value    
        
                
size=3

a=Stack("test",size)

a.push('hello')
a.push('kello')
a.push("baby")
a.pop()
a.stack_is_empty()
a.stack_is_full()
a.check_stack_size()
a.push("apple")
a.peek()
a.ground()
a.push(1)
a.push(2)
a.push(3)

a.check_stack_size()
a.pop()
a.pop()
a.push("top")
a.peek()
a.ground()
a.stack_is_empty()
a.stack_is_full()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
a.clear()
a.push(1)
a.push(2)
temp=a.find('kkk')
print(temp)
value=a.dump()
print(value)


if __name__=="__main__":
    print("내부 실행 모듈")