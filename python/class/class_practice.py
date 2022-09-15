class Fourcla:
    temp="hello"
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def setdata(self,first,second):
        self.first=first
        self.second=second
        
class more_Fourcal(Fourcla):
    
    def __init__(self,first,second):
        Fourcla.__init__(self,first,second)
        self.multiple=self.first*self.second 
        
    def m1(self):
        return self.multiple
    
    def compare(self,a):
        if a==self.temp:
            print("정답")
           
        
number=Fourcla(10, 20)


print(number.first)
print(number.second)


number.setdata(100,200)


print(number.first)
print(number.second)

n1=more_Fourcal(5, 10)
print(n1.multiple)
print(n1.m1())

print(number.temp)

n1.compare("hello")









        