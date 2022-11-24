# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # left = focuse Node
        # rigth = arr last idx
        # 최대 힙 MAX Heap
        temp = a[left]      # 주목하는 노드의 값

        parent = left  # 주목하는 노드의 idx parent = target_node
        while parent < (right + 1) // 2: # right+1 자식노드의 왼쪽의 idx가 존재하는가? parent 가 (right +1 )// 2보다 크다면 parent는 자식노드가없는 노드이다 
            cl = parent * 2 + 1    # 자식노드의 왼쪽 idx 
            cr = cl + 1            # 자식노드의 오른쪽 idx
            child = cr if cr <= right and a[cr] > a[cl] else cl  #자식노드중 큰값의 idx 
            
            if temp >= a[child]: # 부모노드와 자식노드의 대소관계를 비교합니다 
                break # 부모노드가 크다면 값 swap x
            
            a[parent] = a[child] #자식노드가 더크다면 교환 ...부모노드의 자리에 자식노드의 값을 삽입한다 부모노의값은 일단 temp가 저장하고있고 트리에서 덮어씌우기된상태
            parent = child # 집중하고있는곳을 변경한다 자식노드의값에 집중한다.. 왜냐하면 자식노드가 자식노드를 또한가지고있을떄 교환을하기위해서
             
        a[parent] = temp # ....? 원래 temp의 값이있어햘곳에 위치에 삽입한다 

    n = len(a)
    count=0
    for i in range((n - 1) // 2, -1, -1):    #  heapify 과정
        down_heap(a, i, n - 1) # right left 의미 ...?
        print(f"{count}번째 {a}")
        print(i, n-1)
        
        count+=1
    print(a) #MAX_HEADP
    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]   # 맨끝원소와 루트노드의 위치를 교환합니다 정렬이완료된곳과 정렬이아직완료안된부분으로 나뉘어진다..
        down_heap(a, 0, i - 1)    # right 시작 idx left는 정렬이 아직완료안된곳의 맨끝idx
    print(a) 
    
if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    # print('오름차순으로 정렬했습니다.')
    # for i in range(num):
    #     print(f'x[{i}] = {x[i]}')