data = [7,6,5,8,3,5,9,1,6]

# 1단계 haep 상태가아니므로 MAX_HEAP으로 재구성합니다

for i in range(1,(len(data)-1)//2):  # 1부터시작한다 왜냐하면 0루트노드는 상향 부모노드가없개때문에 len(data)-1//2 는 자식노드가 마지막으로 존재하는 노드idx
    target = i # 주목하는 노드
    target_c = (target * 2) +1 # 주목하는노드의 자식 idx
    
    if data[target_c] < data[target_c+1]: # 자식 오른쪽 왼쪽 누가크니?
        target_c+=1 #오른쪽 포커스
        
    if data[target] < data[target_c]: # 부모 자식 비교
        data[target] , data[target_c] = data[target_c] , data[target] #자식이크네? => 부모 자식 교환
    # 위에코드는 하향식으로 진행하며 단 1번만 진행한다 target 과 target의 자식에대해서
    # 아래코드는 상향식으로 진행하며 root노드가 될떄까지 올라간다   
    while target != 0: # 상향식으로 올라간다 부모로 올라간다 target == 0 이라는것은 최상단 root노드이므로 더이상 부모노드가존재하지않으므로 비교를 그만한다
        
        target_p = (target-1)//2 #부모 idx구하기
        if (data[target] > data [target_p]): #부모가크니 주목노드가 크니
            data[target] , data[target_p] = data[target_p] , data[target]  #주목노드가 크다면 주목노드를 부모노드 자리로 자리를 이동한다
        
        
        target = target_p     # 상향식으로 올라간다
    
print(data) #MAX HEAP 구성 

for i in range(len(data)-1,-1,-1):
    data[0] , data[i] = data[i] ,data[0] # 최상단루트의 idx 는 0 번지이다 정렬이 아직안된부분은 배열의 i번째이다 서로 자리교환을한다 그러면 최상단루트는 아래로 가며 정렬된부분으로 분류하겠다
    root = 0 # 최상단 root 시작 idx 
    target = 1
    
    while 2 * root +1 < i : # 자식이 존재하니?? ----> 자식이 존재하면서 아직 자식이 정렬이안된부분이어야한다 만약 자식이 정렬된부분이라면 i범위에 걸린다
        target_child = root * 2 +1 # 자식 idx 
        if (data[target_child] < data[target_child+1] and target_child < i-1): # 왼쪽 오른쪽 누가크니
            target_child+=1 # 오른쪽 포커스 왼쪽보다 오른쪽 자식의 값이 더크다
        # 34 행에서 and조건을 추가하였습니다 왜냐하면 자식노드가 2개있는데 
        # 1개는 정렬이안된부분이고 (왼쪽) 1개는 정렬된부분(오른쪽) 이라면 오른쪽 왼쪽 대소관계를 비교하면 안됩니다
        # 무조건 정렬이안된(왼쪽)이 자식노드로 고정을 해야합니다
        
        
        
        if (data[target_child]>data[root]): # 부모가크니 자식이크니
            data[target_child] , data[root] = data[root] , data[target_child] #자식이 크므로 부모와 자라교환을 진행한다
        root = target_child # 하향식으로 내려간다 언제까지 --->> 정렬이안된자식을 가질때까지
        
        
            
        
print(data)  #HEAP-SROT 완료

        