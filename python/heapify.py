heap=[7,6,5,8,3,5,9,1,6]
number=9
print(heap)
# 먼저 전체트리를 Max HEAP 구조로 변경한다 ....1단계
for i in range(1,number): # 1부터시작하는이유 최상단루트노드제외
    c = i # 주목하는 노드 
    while c!=0:
        root = (c -1)//2; #주목하는 노드의 부모의인덱스를 구하는거고0
        if heap[root] < heap[c]:
            heap[root],heap[c]=heap[c],heap[root]
        c = root
        
print("1단계확인:",heap)
         

for i in range(number-1,-1,-1): #..2단계
    heap[0],heap[i]=heap[i],heap[0] #최상단 루트노의값과 마지막트리의 값의 위치를 교환한다
    root = 0
    c = 1
    
    
    while 2*root+1 < i:
        c = 2 * root + 1
        if (heap[c] < heap[c+1] and c <i-1):
            c+=1

        if (heap[root] < heap[c]):
            heap[root],heap[c] = heap[c],heap[root]
            
        root = c
        
        
        
print(heap)
            
        
    