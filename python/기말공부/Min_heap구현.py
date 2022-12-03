import random
data =[random.randrange(20) for i in range(10)]
print("초기생성",data)

# 일단 자식과의 대소관게를 비교한다
# 그리고 루트노드가될떄까지 부모노드와 비교를한다
# 단 내림차순으로 구현한다  

# 1단계 MIN_HEAP구성하기
for i in range((len(data)-1),-1,-1):
    focus = i
    focus_child = (focus * 2)+1
        
    if focus_child >= len(data): # 자식이없는경우
        pass
    else: # 자식이 한개라도 존재할시
        if focus_child+1 >=len(data): #오른쪽 자식이 존재하는 확인하는코드 
            pass
        else:
            if  data[focus_child] > data[focus_child+1]:  
                focus_child +=1
        if data[focus_child] <data[focus]: # 주목노드가 더 크다면 자리교환 큰값을 밑으로
            data[focus_child], data[focus] = data[focus], data[focus_child]
            
    # 이후 상향식으로 진행
    
    while  focus!=0: #루트노드가 아닌동안
        focus_parent = (focus -1) // 2
        if data[focus_parent] > data[focus]: # 큰값을 밑으로 부모가 크다면 자리교환
            data[focus_parent] , data[focus] = data[focus], data[focus_parent]
        
        focus = focus_parent
print("Min_heap 구성완료",data)


        
#2단계 Heapify과정을 수행하며 힙정렬을 수행한다
#단 내림정렬이다

for i in range(len(data)-1,-1,-1):
    data[0] , data[i] = data[i], data[0]
    root = 0
    
    while root*2 +1 < i :  #  어떤노드의 자식노드가  정렬된 i부분을 넘지않는동안
        focus_child = (root*2) +1
        
        if focus_child+1 >=i:
            pass
        else:
            if data[focus_child] > data[focus_child+1]:
                focus_child+=1
        
        if  data[root] > data[focus_child]:
            data[root] , data[focus_child] = data[focus_child], data[root]
            
        root = focus_child
        
        
print("Min정렬 구성완료",data)
            
                