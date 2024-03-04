def add(a,b):
    return a+b
def multiple(a,b):
    return a*b

class Unit():
    def __init__(self,name):
        self.name=name
    def my_name(self):
        print(f"나의 이름은 {self.name}입니다")   
        
class Unit_plus(Unit):
    def __init__(self, name,height):
        Unit.__init__(self, name)
        self.height=height
        
    def my_name(self):
        print("나의 이름은 {0}이고 키는 {1}입니다".format(self.name,self.height))
        
        
class Unit_plus_alpha(Unit_plus):
    def __init__(self, name, height,weight):
        Unit_plus.__init__(self, name, height)
        self.weight=weight
        
    def my_name(self):
        print("나의 이름은 {0}이고 키는{1} 몸무게는 {2}입니다".format(self.name,self.height,self.weight))
        
        
                        
