from typing import Any
class FixedStack(object):
    
    class Empty(Exception) :
        pass
    
    class Full(Exception):
        pass
    def __init__(self,capacity=10)->None:
        self.capacity=capacity
        self.stk=[None for _ in range(capacity)]
        self.point=-1 #포인트를 -1로잡앗다 스택이 한개쌍히면 배열과 포인터 모두 0이된다
        
        """
        push작동
        stk[point+1]=data
        point+=1
        """
        
    def __len__(self):
        return self.point
    
    def __contains__(self,value): #해당 vlaue가 stk안에 존재하나여??
        res=self.count(value)
        if res==0:
            return False
        else:
            return True
    
    def is_empty(self)->bool: #스택이 비어있는지 검사합니다
        if (self.point<=-1): #포인터가 -1보타 작다는것은 스택이 empty라는것이다
            return True
        return False
    
    def is_full(self)->bool: # 만약 욜량이 5이고 배열이[5]번까지차있으며 point=5이다
        if(self.point>=self.capacity):# 포인터가  용량과같거나 커지는순간 full이다
            return True
        return False
    
    def push(self,value): #스택에다가 데이터를 쌓는다
        if(self.is_full()==True):
            raise self.Full #사용자 정의 에러발생 스택이 풀일시 데이터삽입이 불가하다
        self.stk[self.point+1]=value 
        self.point+=1 #stk에저장된곳에 하나 뒤떨어진곳을 지칭하고있다
        
    def pop(self): #스택에서 데이터를 하나꺼내며 원소를 반환한다
        if(self.is_empty()): #스택이 empty상태라면 pop이불가하다
            raise self.Full
        data=self.stk[self.point]
        self.stk[self.point]=None
        self.point-=1
        print("stack locpop {}".format(data))
        return data 
    
    def peek(self): #스택의 탑의 원소를 확인하며 원소삭제는 이루어지지않는다
        if(self.is_empty()): #스택이 empty라면 peek가불가하다
            raise self.Empty
        res=self.stk[self.point]
        print("peek:{}".format(res))
        return res 
    
    def clear(self): #스택의 원소를 전부 empty상태로 만든다
        for i in range(self.point+1): 
            self.stk[i]=None
        self.point=-1
        print("clear stack")
        
    def count(self,value) ->int: #스택의 동일원소의 개수를 확인한다
        count=0
        for i in range(self.point,-1,-1):
            if self.stk[i]==value:
                count+=1
        print("stk in elem {} count {}".format(value,count))
        return count
    
    def find_location(self,value): #스택에 있는 사용자가입룍한 value의 모든 원소의 index를 return한다
        buffer=list()
        if(self.is_empty()):
            raise self.Empty
        for i in range(self.point,-1,-1):
            if self.stk[i]==value:
                buffer.append(i)
        print("find_location value {} buffer {}".format(value,buffer))
        return buffer
    
    def dump(self):
        buffer=list()
        if(self.is_empty()):
            raise self.Empty
        
        for i in range(self.point,-1,-1):
            buffer.append(self.stk[i])
    
        print("dump {}".format(buffer))
        return buffer        
    
    def stack_status(self):
        print("현재 스택의 갯수는 {}입니다".format(self.point+1))  
    
    

if __name__=="__main__":
    stack=FixedStack(10)  
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    stack.pop()
    stack.dump()
    stack.peek()
    stack.count(4)
    stack.find_location(4)
    stack.stack_status()
    stack.dump()
    stack.clear()
    stack.stack_status()
