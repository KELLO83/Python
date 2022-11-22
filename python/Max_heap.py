# 1단계 전체트리구조를 MAX_HEAP로 변경한다
# 2단계 크기를 줄여가며 힙을구성한다
# Heapify 수행할떄마다 O(log N) 소요 트리의 높이만큼만 진행하면된다
# Heapfiy 과정을 리스트의 원소의 갯수만큼만 진행하면 MAX_HEAP구성완료

data = [7,6,5,8,3,5,9,1,6]
# data=[9,8,7,6,3,5,5,1,6] -> 1단게를 완료후 나와야하는 결과
# [9, 7, 8, 6, 3, 5, 5, 1, 6]
print(data)
print("heapify수행 횟수",len(data)//2)

#1단계 전체트리를 MAX_Heap 구조로 변경을한다


for i in range(1,len(data)//2):
    target = i
    target_child = (target * 2) + 1
    target_parent = (target-1) // 2
    #일단 자식노드의 값과 비교하여 자리스왑여부를정한다
    if ( data[target_child] < data[target_child+1]):
         target_child = target_child + 1
    if (data[target] < data [target_child] ):
        data[target] , data[target_child] = data[target_child] , data[target]
        

    while target !=0:
        target_parent = (target-1) // 2
        if (data[target] > data[target_parent]):
            data[target] , data[target_parent] = data [target_parent] ,data[target]
        target = target_parent
        
print("MAX_HAAP 구성완료후",data) 

#2단계 크기를줄여가면서 힙정렬을 실시한다

for i in range(len(data)-1,-1,-1):
    data[0] , data[i] = data[i] ,data[0]
    root = 0
    target = 1
    
    while 2 * root +1 < i : #자식이 존재한다면?
        pass          
        










# for i in range(1,len(data)):
#     target = i
#     while target!=0:
#         target_parent = (target - 1) // 2 #주목하는 노드의 부모의 idx
#         if data[target_parent]<data[target]: #부모노드의값이 주목하는 노드 (자식)보다 작다면
#             data[target_parent],data[target] = data[target],data[target_parent] #자리교환을한다
            
#         #상향식정렬 
#         target  = target_parent
        
# print(data)