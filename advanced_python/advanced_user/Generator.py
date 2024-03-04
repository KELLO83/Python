#iterable객체 =>반복가능한 객체
# list dict str bytes tuple range
#lterator 값을 차례대로 꺼낼수있는 객체

def countdown(n):
    while n>0:
        yield n
        n=n-1
x=countdown(5)
print(x) #generator객체 

for i in range(5):
    print(x.__next__())
    
def multi_generator(n):
    data=[1,2]
    
    while n>0:
        yield from data #한번 retunr할때 리스트를 한꺼번에 return한다
        n=n-1
        
        
x=multi_generator(5)
print(list(x))