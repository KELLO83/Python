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
        p = self.root           # 스캔 중인 노드
        parent = None           # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return False    # 그 키는 존재하지 않음

            if key == p.key:    # key와 노드 p의 키가 같으면
                break           # 검색 성공
            else:
                parent = p                  # 가지를 내려가기 전에 부모를 설정
                if key < p.key:             # key 쪽이 작으면
                    is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
                    p = p.left              # 왼쪽 서브 트리에서 검색
                else:                       # key 쪽이 크면
                    is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
                    p = p.right             # 오른쪽 서브 트리에서 검색

        if p.left is None:                  # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:               # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent = p
            left = p.left                   # 서브 트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key                # left의 키를 p로 이동
            p.value = left.value            # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left     # left를 삭제
            else:
                parent.right = left.left    # left를 삭제
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
    
        
            
                
if __name__ =="__main__":
    B1= BinarySearchTree();
    B1.add(5,"HELLO")
    B1.add(10,"Hello")
    B1.add(15,"TE")
    B1.add(20,"KELLO")
    print(B1.max_key())
    B1.add(3,"Dsban")
    print(B1.min_key())
    