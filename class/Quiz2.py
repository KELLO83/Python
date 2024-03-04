class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0}Unit generation".format(name))
        
    def move(self,location):
        print("{0} : {1} move location speed={2}".format(self.name,\
            self.locaion,self.speed))
    
    def damaged(self,damage):
        print("{0} : {1} damged".format(self.name,damage))
        self.hp=self.hp-damage
        print("{0} reamin hp {2}".format(self.name,self.hp))
        if self.hp<=0:
            print("remain hp zero distroy")     
                    

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage     
        
    def damaged(self,damage):
        print("{0} : {1} damged".format(self.name,damage))
        self.hp=self.hp-damage
        print("{0} reamin hp {2}".format(self.name,self.hp))
        if self.hp<=0:
            print("remain hp zero distroy")     
            
            
            
class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"Marin", 40, 1, 5)          
        
    def stimpack(self):
        if self.hp>10:
            self.hp=self.hp-10    
            print("stimpack use")
            self.speed=self.speed+10
        else:
            print("remain hp not enough stimpack unuse")   
            

class Tank(AttackUnit):
    seize_develop=False

    def __init__(self):
        AttackUnit.__init__(self,"Tank",150,1,35)                   
        self.seize_mode=False
        
    def set_seiz_mode_on(self):
        if Tank.seize_develop==False:
            print("seize mode not develop")
            return
        else:
            print("seize mode on")
            self.damage=self.damage+100
            self.speed=0
            self.seizemode=True
            
    def set_seiz_mode_off(self):
        if  self.seizemode==False:
            print("not seize mode")
            return    
        else:
            print("seiz mode off")
            self.seizemode==False
            self.damage=self.damage-100
            self.speed=1
            
            
class Flyable(Unit):
    def __init__(self, name, hp , speed, flying_speed):
        Unit.__init__(self, name, hp, speed)
        self.flying_speed=flying_speed            
    
    def fly(self,name,location):
        print("{0} {1} move fly speed={2}".format(self.name,location,\
            self.flying_speed))
        
    
              
class Flyable_AttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage, speed, flying_speed):        
        AttackUnit.__init__(self,name, hp , 0    ,damage)        
        Flyable.__init__(self   ,name, hp , speed, flying_speed)
        
    def move(self,location):    
        self.fly(self.name, location)
        

class Wraith(Flyable_AttackUnit):
    clocking_develop=False
    def __init__(self, speed):
        Flyable_AttackUnit.__init__(self,"Wraith",80, 20, 5, speed)
        self.clocked=False
        
    def clocking_on(self):
        if clocking_develop==False:
            print("not develop clocking")
            return
        else:
            self.clocked=True
            print("Wraith clocked on")
            
    def clocking_off(self):
        if clocking_develop==False:
            print("not develop clocking")
        else:
            self.clocked=False
            print("clocked off")
            
            
# m1=Marin()
# m2=Marin()
# m3=Marin()
# t1=Tank()
# t2=Tank()


w1=Wraith(100)
w2=Wraith(200)


