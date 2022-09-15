class Unit:
    def __init__(self,name,hp,damage):#init 
        self.name=name
        self.hp=hp
        self.damage=damage
        
        print("{0}유닛이 생성되었습니다".format(self.name))
        print (f"체력{hp} 공격력{damage}\n")
        

class AttackUnit:
    def __init__(self,name,hp,damage):#init 
        self.name=name
        self.hp=hp
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
        
                 
firebat1 =AttackUnit("dog",50, 16)
firebat2 =AttackUnit("cat",100, 26)

firebat1.attack("5시")
firebat1.damaged(25)
firebat2.damaged(20)




