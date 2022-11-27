data = [7,6,5,8,3,5,9,1,6]
#[7, 8, 9, 6, 3, 5, 5, 1, 6]
# 1단계 haep 상태가아니므로 MAX_HEAP으로 재구성합니다

for i in range((len(data)-1)//2 , -1 ,-1):  # 1부터시작한다 왜냐하면 0루트노드는 상향 부모노드가없개때문에 len(data)-1//2 는 자식노드가 마지막으로 존재하는 노드idx
    target = i # 주목하는 노드
    target_c = (target * 2) +1 # 주목하는노드의 자식 idx
    
    if target_c > len(data)-1:
        continue
    
    if data[target_c] < data[target_c+1] : # 자식 오른쪽 왼쪽 누가크니?
        target_c+=1 #오른쪽 포커스
        
    if data[target] < data[target_c]: # 부모 자식 비교
        data[target] , data[target_c] = data[target_c] , data[target] #자식이크네? => 부모 자식 교환
    
    target = target_c
    
    while target < (len(data)-1)//2:
        target_c = target *2 +1
        
        if data[target_c] < data[target_c+1] and target_c+1 > len(data):
            target_c +=1
            
        if data[target] < data[target_c]:
            data[target] , data[target_c] = data[target_c] , data[target]
        
        target = target_c
            
print(data) # MAX_HEAP 구성

for i in range(len(data)-1,-1,-1):
    data[0] , data[i] = data[i] , data[0]
    target = 0
    
    while 2*target+1 < i:
        target_c = target * 2+1
        if (data[target_c] < data[target_c+1] and target_c+1 < i):
            target_c +=1
            
        if (data[target] < data[target_c]):
            data[target_c] , data[target] = data[target] , data[target_c]
        
        target = target_c       
print(data)
                