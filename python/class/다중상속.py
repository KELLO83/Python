class Unit:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        

class AttackUnit(Unit):#상속
    def __init__(self,name,hp,damage):
        Unit.__init__(self, name, hp)  
        self.damage=damage
        
        print("{0}유닛이 생성되었습니다".format(self.name))
        print (f"체력{hp} 공격력{damage}\n")
        
    def attack(self,location):
        print("{}:{} 방향으로 공격중 공격력{}".format(\
                self.name,location,self.damage))
    
    
    def damaged(self,dameage):
        print("{}:{}데미지를 입었습니다".format(self.name,dameage))
        self.hp=dameage
        print("{}:현재체력은 {}입니다".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}:파고되었습니다",format(self.name)) 
        

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
        
    def fly(self,name,location):
        print("{}:{}방향으로 날아갑니다 속도{}".format(name,location,self.flying_speed))    
        
class Flyable_attack(AttackUnit,Flyable):#다중 상속
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
       
        

                
        



valkyrie=Flyable_attack('발키리', 200, 6, 5)

valkyrie.fly(valkyrie.name,"3시")


