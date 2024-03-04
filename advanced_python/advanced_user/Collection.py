#collection module

import collections


point=collections.namedtuple("Naming",['x','y']) #기존 tuple에 위치인덱스 대신 이름으로 필드 접근가능
K1=point(10,20)
print(K1)

print(K1.x+K1.y) #K1.속성 접근가능
print(K1[0]+K1[1]) #또는 인덱싱으로 접근가능

#-------------------------------------


def Queue(): #FIFO 구조
    data=collections.deque()
    for i in range(1,6): #1,2,3,4,5
        data.appendleft(i)       
    for i in range(len(data)):
        data.pop()
        
def Circle_Queue():
    data=collections.deque()
    for i in range(1,6): #1 2 3 4 5 
        data.append(i)
    print(data)
    data.rotate(2) #두칸씩 미루기
    print(data)

def new_deque():
    data=collections.deque("Hello")
    for i in data:
        print(i)
    print()    
    
def Stack()->None:
    """ FILO """
    data=collections.deque()
    for i in range(1,6):
        data.append(i)
    for i in range(len(data)):
        print(data.pop(),end="")    



text='message'
count=collections.Counter(text) #Sequence자료형의 데이터값의 개수를 dict형태로 반환한다
print(count)
print(count['m']) #m의갯수 


data=collections.OrderedDict() #순서가있는 dict형태

data['a']=100
data['b']=300
data['c']=200

print(data)





        