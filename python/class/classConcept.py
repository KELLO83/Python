class animal:    
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print("모든 생물은 소리는 낼것이다")
        
        
        
class dog(animal):
    def __init__(self, name):
        animal.__init__(self, name)
    
    def sound(self):
        print('{}는 멍멍~~~'.format(self.name))
        
class cat(animal):
    def __init__(self, name):
        animal.__init__(self, name)
    
    def sound(self):
        print("{}는 야용~~~" .format(self.name))
        
        
        
class superDog(dog):
    def __init__(self, name, dish):
        dog.__init__(self, name)
        self.dish = dish
        
    def like(self):
        print('{}는 {}를 좋아해'.format(self.name, self.dish))
        

class robotDog(superDog):
    def __init__(self, name, dish):
        superDog.__init__(self, name, dish)
        
    def run(self, speed):
        print("{}는 {}를 좋아해서 {}의 속도로 달려~~".format(self.name, self.dish, speed))
        
    def plus(self, a, b):
        return a +b
    
    
class cal:    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2    
    def run(self):
        print("계산할거임")
    
    
class add(cal):    
    def __init__(self, n1, n2):
        cal.__init__(self, n1, n2)
        
    def run(self):
        print("{} + {} = {}".format(self.n1, self.n2, self.n1 + self.n2))


class sub(cal):    
    def __init__(self, n1, n2):
        cal.__init__(self, n1, n2)
        
    def run(self):
        print("{} - {} = {}".format(self.n1, self.n2, self.n1 - self.n2))
        

a = add(10,20)        
a.run()
    
b = sub(10,20)        
b.run()
    
    
        
        
# d = dog('강아지')
# d.sound()

# c = cat('고양이')        
# c.sound()

# sd = superDog('슈퍼강아지', '고기')
# sd.sound()
# sd.like()

# rd = robotDog('로봇독', '건전지')
# rd.run(50)

# print(rd.plus(10,20))
    
        
        
