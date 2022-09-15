class Person:
    
    maxAge = 200
    maxSpeed = 100
    
    def __init__(self, name):
        self.name = name
        
    def run(self, speed):
        if speed >= self.maxSpeed: 
            print("죽었습니다!")
        else: 
            print(f'{self.name}이 {speed}의 속도로 달립니다!')
        
        
class Male(Person):
    
    military = True
    def __init__(self, name):
        Person.__init__(self, name)
        self.military = True
    
    def recruit(self):
        if self.military: print("ㅉㅉ")
        else: print("ㅋ")
        
    def run(self, speed):
        print("군인이 달리냐?")
    
    
    
    
    
a = Person("송")
print(a.maxSpeed)
a.run(80)
a.run(120)

b = Male("송준현")
b.recruit()
b.run(30)