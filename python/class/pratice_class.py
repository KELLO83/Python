class Unit:
    def __init__(self,name,hp,damage):#init 
        self.name=name
        self.hp=hp
        self.damage=damage
        
        print("{0}유닛이 생성되었습니다".format(self.name))
        print (f"체력{hp} 공격력{damage}\n")
        


# marin1=Unit("마린",40,5) 

# marin2=Unit("마린2",40,5)

# tank=Unit("탱크",150,35)

# marin3=Unit("탱크2", 150, 35)

 
wraith1=Unit("레이스", 80, 5)

print("유닛이름:{} , 공격력{}".format(wraith1.name,wraith1.damage))

wraith2=Unit("뺴앗은 레이스",80, 5)
wraith2.clocking=True

if wraith2.clocking==True:
    print("{}는 클로킹 상태".format(wraith2.name))
    