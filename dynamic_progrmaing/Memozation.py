def solution(Max_Weight:int,gold_weight:list,gold_price:list):
    gold_bar_size = len(gold_price)
    memorization = [[0 for i in range(MAX_WEIGHT+1)] for j in range(gold_bar_size+1)]
    for i in range(1,gold_bar_size+1): # 0원 자동 초기화 row scan
        print(i-1,'개---->',end=' ')
        for j in range(Max_Weight+1): #Colum scan ----> 가방무게 
            if gold_weight[i-1] > j : # 현재 스캔중인 골드무게가 가방보다 무거오면 넣기 불가
                memorization[i][j] = memorization[i-1][j] # 현재행열에 이전행열의 가격을 넣는다 memo
                
            else: # 현재 스캔중인 골드무게를 가방에 넣을수있으면
                memorization[i][j] =  gold_pirce[i-1] + memorization[i-1][j-gold_weight[i-1]] 
                # 일단 현재스캔중인 골드바의 가격을넣고 + 남은무게만큼 이전행의 열값에서 더함 
                
                if memorization[i][j] < memorization[i-1][j]:
                    memorization[i][j] = memorization[i-1][j]
            print('{}'.format(memorization[i][j]),end=' ')
        print()
                    

if __name__ == "__main__":
    gold_weight = [0,6,4,3,5]
    gold_pirce = [0,13,8,6,12]                                   
    MAX_WEIGHT = 7
    solution(MAX_WEIGHT,gold_weight,gold_pirce)
    