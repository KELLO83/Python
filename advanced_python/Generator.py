def countdown(n):
    while n>0:
        yield n #return은 하되 다음호출시 n=n-1실행
        n=n-1
def range__(n):
    i=0
    while(i<n):
        yield i
        i=i+1
for x in countdown(10):
    print(x,end=" ")

print()
    

for x in range__(10):
    print(x,end=" ")    
    
    
x=countdown(10)
print()
print(x) #x=Genrator




class MyItercls:
    def __init__(self) -> None:
        self.data=[]
    def __iter__(self):
        return self.data.__iter__()
    


seq=MyItercls()
for e in seq:
    print(e,end=" ")
