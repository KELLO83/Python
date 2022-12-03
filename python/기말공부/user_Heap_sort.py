import random
data = [ random.randrange(20)  for i in range(10)]
print("초기생성",data)
# 방향 윗방향
# 1단계 MAX_Heap 구성하기
# 세부사항
#   일단 주목노드와 주목노드의 자식과 값을 비교여부를 정한다
for i in range((len(data)-1)//2,-1,-1):
    focus_node = i # 주목노드
    focus_node_c = ( focus_node * 2 ) +1 #주목노드의 오른쪽 자식 포커스
    
    if focus_node_c  >= len(data): #out of range 발생시 자식노드가 존재하지않으므로 바로 상향식으로올라간다
        pass # 자식이존재하지않으므로 자식간의 대소관계를 비교하지않는다
    
    else: #자식이 적어도 1개이상 존재한다
        if focus_node_c+1 < len(data):
            if data[focus_node_c] < data[focus_node_c+1] : # 자식노드의 왼쪽 오른쪽의 대소관게를 비교하면 오른쪽이 존재하는지도 확인한다
                focus_node_c +=1 
                
        if data[focus_node_c] > data[focus_node]: #  주목노드의 자식과 주목노드의 대소관계를 비교한다
            data[focus_node_c] , data[focus_node] = data[focus_node] , data[focus_node_c]

    while focus_node!=0: # 주목노드가 root 노드가 아닐떄까지 방향 윗방향
        focus_node_p = (focus_node-1)//2
        if data[focus_node_p] < data[focus_node]:
            data[focus_node] , data[focus_node_p] = data[focus_node_p], data[focus_node]
            
        focus_node = focus_node_p
print("MAX_HEAP구성",data)

#2단계 정렬시키기

for i in range(len(data)-1,-1,-1):
    data[i] , data[0] = data[0] , data[i]
    root =0 # 상향식 방향으로써 항상0 에서 시작하며 내려간다    
    while root * 2 +1 < i: # 자식이 정렬이안된부분의 범위를 넘어서지않은한
        target_c= root *2 +1 
        if data[target_c] < data[target_c+1] and target_c+1 < i:
            target_c+=1   
            
        if data[root] < data[target_c] :
            data[root] , data[target_c] = data[target_c] ,data[root]
        
        root = target_c       
    
print(data)    
    