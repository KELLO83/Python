def knapsack():
    print("Memozation")
    array = [[0 for _ in range(maxWeight+1)] for _ in range(rowCount+1)] 
    print(array)
    
    for row in range(1,rowCount+1):
        print(row,'개-->',end="")
        for col in range(1,maxWeight+1):
            if weight[row] > col: # if (가져올무게 > 현재배낭무게)
                array[row][col] = array[row-1][col] # 바로 윗행의 결과를 그대로가져온다
                
            else: # if (금괴무게 <= 현재배낭무게)
                value1 = money[row]+array[row-1][col-weight[row]] # 앞행[row-1]의 [현재배낭무게-금괴무게]열의 가격 
                value2 = array[row-1][col] # 자기행의 바로윗행의 가격
                array[row][col] = max(value1,value2) # 윗행이크니 내가크니 판별해서 큰값을 현재 작업배열에 넣는다
            print('%2d'%array[row][col],end=" ")
        print()
    print("메모제이션 배열")
    print(array)
    return array[rowCount][maxWeight]    



maxWeight = 7 # 행 무게
rowCount = 4 #  열 보석의 갯수 
weight = [0,6,4,3,5]
money = [0,13,8,6,12]


maxValue = knapsack()
print()
print("배낭에 담을수있는 보석의 최대가격 --->",maxValue)


