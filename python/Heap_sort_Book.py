# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # left = focuse Node
        # rigth = arr last idx -> 아직 모든부분이 정렬이 완료된상태가아니므로 arr  last idx 는 배열의 맨끝 원소의 idx입니다
        
        # 최대 힙 MAX Heap
        temp = a[left]      # 주목하는 노드의 값
        parent = left  # 주목하는 노드의 idx parent = target_node
        
        # right 는 배열의 맨끝원소의 idx번호입니다 -> (right+1)//2 보다작은 parent는 자식노드가 존재하며 (right+1)//2 보다 크거나 같아지면 자식노드가 존재하지않습니다
        while parent < (right + 1) // 2: # right+1 자식노드의 왼쪽의 idx가 존재하는가? parent 가 (right +1 )// 2보다 같거나 크다면 parent는 자식노드가없는 노드이다 
            cl = parent * 2 + 1    # 자식노드의 왼쪽 idx 
            cr = cl + 1            # 자식노드의 오른쪽 idx
            child = cr if cr <= right and a[cr] > a[cl] else cl  #자식노드중 큰값의 idx 
            
            if temp >= a[child]: # 부모노드와 자식노드의 대소관계를 비교합니다 
                break # 부모노드가 크다면 값 swap x
            
            a[parent] = a[child] #자식노드가 더크다면 교환 ...부모노드의 자리에 자식노드의 값을 일단 삽입합니다 주목노드의값은 일단 temp가 저장하고있고있습니다
            parent = child # 집중하고있는곳을변경한다 검사 대상은 주목노드의 자식노드로 변경합니다 -> 하향식으로 내려갑니다 언제까지? 주목노드가 자식노드가없을떄까지
             
        a[parent] = temp # parent는 자식노드가 없는곳에서 멈춥니다 그위치에 원래 주목하는노드값이 가지고있던 데이터값을 삽입합니다

    n = len(a)
    count=0
    for i in range((n) // 2, -1, -1):  # (n-1)//2 
        down_heap(a, i, n - 1) 
        print(f"{count}번째 {a}")
        print(i, n-1)
        
        count+=1
        
    print(a) #MAX_Heap
    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]   # 맨끝원소와 루트노드의 위치를 교환합니다 정렬이완료된곳과 정렬이아직완료안된부분으로 나뉘어진다..
        down_heap(a, 0, i - 1)    # right root 노드  idx left는 정렬이 아직완료안된곳의 맨끝idx
    print(a) 
    
if __name__ == '__main__':
   data = [7,6,5,8,3,5,9,1,6]
   heap_sort(data)
   