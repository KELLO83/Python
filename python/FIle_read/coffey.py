#coffey. py

coffee=10
money=400
return_money=0

while True:
    if money==300:                                                                                                                                                                                          
        print("커피를 줍니다")
        coffee=coffee-1
    elif money>300:
        return_money=money-300
        print("거스름돈 %d를 줍니다"%return_money)
        money=money-300
        print("현재 남은돈은 %d입니다"%money)
        coffee=coffee-1
    else:
        print("돈이 부족합니다 300원이상주세요")
        print("남은 커피의 양은 %d개입니다"%coffee)
    if coffee==0:
        print("커피가 다떨어짐")
        break
    
    
      