coffee=10

money=0
return_money=0
while True:
    money=int(input("돈을 넣어주세요"))
    if money==300:
        print("커피를 줍니다")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d를 줍니다"%(money-300))
        print("커피를 줍니다")
        coffee=coffee-1
        
            
    else:
        print("소지금이 부족합니다")
        break
        
    if coffee==0:
        print("커피가 부족합니다")
        break


    