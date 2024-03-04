"""
이진검색트리 구현
조건
1) 왼쪽 노드의 키값은 주목노드의 키값보다 작아야한다 주목노드 키값 > 주목노드 왼쪽자식의 키값
2) 오른쪽 노드의 키값은 주목노드의 키값보다 커야합니다 주목노드 키값 < 주목노드 오른쪽자식의 키값
3 )키값 중복인 노드는 허락되지않습니다
4) 중앙순회시 키값 오름차순이 가능합니다

"""
from typing import *
class Node:
    def __init__(self,key,value=None,left=None,right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None  # 루트노드 일단 EMPTY
        
    def search(self,key):
        "key를 가지는 노드검색"
        p =self.root # 루트노드부터 시작한다
        while True:
            if p is None: # 검색실패
                return None

            if key == p.key:
                print("해당노드의 메모리주소",p)
                return p.value

            elif key < p.key:
                p = p.left # 찾고자하는 key값이 주목노드의 key값보다 작은경우 왼쪽으로
                
            elif key > p.key:
                p = p.right # 찾고자하는 key값이 주목노드의 key값보다 큰경우 오른쪽으로
                
    def add(self,key,value):
        
        
        def add_node(node:Node,key:int,value:int) ->bool:
            """ 적어도 루트노드이상 존재할떄 call되는 함수"""
            if key == node.key: # 주목노드가 삽입할려는 노드key값인경우 중복적으로 삽입이 불가하므로 삽입 fail
                return False
            
            elif key < node.key: # 삽입할려는key값이 주목노드의 key값보다 작을경우 왼쪽으로 
                if node.left is None: # 왼쪽으로 진행한다 주목노드의 left가 None이라면 왼쪽자식이 없으므로 삽입한다
                    node.left = Node(key,value,None,None) # 주목노드이 왼쪽에다가 새로운 노드를 할당한닺
                else: # 주목노드의 왼쪽자식이 존재하므로 왼쪽으로 또이동해야함 
                    add_node(node.left,key,value) # 인수로 주목노드는 현재 주목노드의 왼쪽을준다 재귀적으로 호출하며 자식의 왼쪽이 Empty인경우까지 계속 재귀를 진행한다
            elif key >node.key: # 삽입할려는 key값이 주목노드의 key값보다 큰경우 오른쪽자식으로 추가를해야한다
                if node.right is None:
                    node. right = Node(key,value,None,None)
                else:
                    add_node(node.right,key,value)
                return True # 성공적으로 key값의 노드를 삽입하였습니다
            
        
        if self.root is None: # 초기노드가 존재 x일시
            self.root = Node(key,value,None,None) # rigth left None 
            return True # 노드삽입완료
        else: #노드가 적어도 루트노드이상 존재한다 
            return add_node(self.root,key,value)
        
    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root       # 루트부터 시작
        parent = None           
        is_left_child = True  

        while True: # 삭제대상 p노드를 찾는과정
            if p is None:       
                return False    

            if key == p.key:   
                break          
            else:
                parent = p            
                if key < p.key:     # 현재노드 p에서 찾고자하는 key값을가진노드가 작을경우 왼쪽으로 이동합니다
                    is_left_child = True   # 왼쪽 서브트리로 이동하였습니다 
                    p = p.left            
                else:                       
                    is_left_child = False   #오른쪽 서브트리로 이동하였습니다
                    p = p.right        

        if p.left is None:            #왼쪽자식이 없다면
            if p is self.root: # 삭제대상이 루트라면
                self.root = p.right #루트는 오른쪽으로 이동합니다
            elif is_left_child: # 왼쪽서브트리로 이동해서 삭제노드p를 찾았다
                parent.left = p.right     # 삭제노드의 p의 부모의 왼쪽과 p의자식인 오른쪽을 이어줍니다
            else:
                parent.right = p.right #오른쪽 서브트리로 이동해서 삭제노드p를 찾았다 -> 부모의 오른쪽과 p의 자식인 오른쪽을 이어줍니다
                
        elif p.right is None:    #오른쪽 자식이 없다면
            if p is self.root: # 삭제대상이 루트라면
                self.root = p.left #루트는 왼쪽으로 이동합니다
            elif is_left_child: # 왼쪽서브트리에서 삭제노드 p를찾았다
                parent.left = p.left     #부모의 왼쪽과 삭제노드 p의자식인 왼쪽을 이어줍니다
            else: # 오른쪽 서브트리에서 삭제노드 p를 찾았다
                parent.right = p.left  #부모의 오른쪽과 삭제노드 p의자식의 왼쪽을 이어줍니다
        else:    # 삭제노드p가 왼 오른 자식을 전부가졌을떄
            parent = p
            left = p.left               
            is_left_child = True #초기시작시 왼쪽으로 이동하였으므로 True입니다
            while left.right is not None: # p노드다음으로 key값이 가장큰 Node를 찾는과정
                parent = left
                left = left.right
                is_left_child = False #계속 오른쪽 서브트리로 이동하므로 False입니다

            p.key = left.key     #덮어쓰기를 진행합니다
            p.value = left.value       
            if is_left_child: #왼쪽서브트리로 이동
                parent.left = left.left   
            else:# 오른쪽서브트리로 이동
                parent.right = left.left   
        return True
            

    def dump(self):
        """모드노드의 ket값을 작은노드부터 탐방하며 각 노드의 data값을 출력합니다"""
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left) # 재귀적 구현 일단 왼쪽으로 가장 파고든다
                print('{} {} '.format(node.key,node.value)) # 이후 중간노드 출력하고
                print_subtree(node.right) # 재귀적 구현 그다음 오른쪽으로 가장 파고든다
        print_subtree(self.root)
        
    def min_key(self):
        """ 노드의 가장 작은키"""
        if self.root is None: # 노드가 한개도존재하지않는다
            return None
        p = self.root # 노드가 적어도 한개이상존재하고 p를 루트노드 시작점으로 잡는다
        while p.left is not None: # left로 쭉파고드는것이 해당 이진트리의 가장작은 node key값이다
            p = p.left #계속 왼쪽으로간다
        return p.key # 노드의 key값을 반환한다
    
    def max_key(self):
        """ 노드의 가장큰 key값"""
        if self.root is None: # 노드갛 한개라도 존재하지않는다
            return None 
        p = self.root # 노드가 적어도 한개이상 존재하므로 주목노드를 일단 root노드로 잡는다
        while p.right is not None: # 오른쪽으로 쭉파고들면서 None일떄까지가면 가장큰KEY값을가진 node를 찾는다
            p = p.right # 쭉파고들기 오른쪽으로
        
        return p.key
    
        
