class Node:
    def __init__(self,data,next):
        self.data = data # 노드에 들어갈 데이터
        self.next = next # 노드다음링크

class LinkedList:
    def __init__(self) -> None:
        self.no = 0 # 노드의갯수
        self.head = None  #머리노드
        self.current = None # 주목노드
        
    def __len__(self):
        return self.no
    
    def search(self,data):
        cnt = 0
        ptr = self.head
        while ptr is not None: # PTR == NONE 은 현재 PTR이 꼬리노드이다 그러므로 NEXT존재X 
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt +=1
            ptr = ptr.next # 주목노드의 NEXT로 이동한다
        return -1 #  데이터값을 찾지못하였다 Fail
    
    def __contains__(self,data):
        return self.search(data) >= 0 
    
    
    def add_first(self,data):
        ptr = self.head # ptr에다가 일단 헤드포인터를 삽입한다
        self.head = self.current = Node(data,ptr)
        self.no += 1
        
    def add_last(self,data):
        if self.head is None:
            self.add_first(data); # head가 None이라면 노드가 한개도 존재하지않는다
        else: # Node가 1개이상 존재
            ptr = self.head 
            while ptr.next is not None: # 마지막 노드를 찾기
                ptr = ptr.next
            ptr.next = self.current = None(data,None) # 마지막노드에 노드를생성후 ptr 포인터의 Next속성에 대입한다

    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next # head.next 가 주목노드이면서 헤드노드가된다
            self.no -=1        
    
    def remove_last(self):
        if self.head is not None: # 노드가 적어도 1개이상존재하며
            if self.head.next is None: # 헤드노드의 NEXT 가 존재X
                self.remove_first() # 노드는 오로지1개
            else:
                ptr = self.head  # 선행
                pre = self.head # ptr후방추적
                
                while ptr.next is not None: # 꼬리노드를 찾는과정
                    pre = ptr
                    ptr = ptr.next    
                pre.next =None # pre.next = ptr pre.next = None 링크절단
                self.current = pre # 주목노드를 pre로 변경한다
                self.no -=1 
    def remove(self,p:Node):
        if self.head is not None: # 노드가 적어도 1개이상 존재하면서
            if p is self.head: # 찾고자하는 노드 p 가 헤드노드라면
                self.remove_first() # 첫번쨰노드제거
            else:
                ptr = self.head
                
                while ptr.next is not p: # p노드이전까지 ptr이 간다
                    ptr = ptr.next
                    if ptr is None: # 찾지못함
                        return
                    ptr.next = p.next # 주목노드의 이전인 ptr 의 next속성을 찾고자하는 노드의 next와 연결시켜서 링크를 절단한다
                    self.current = ptr # 주목노드는 ptr 노드
                    self.no -= 1
                    
    def remove_current_node(self):
        self.remove(self.current)
    
    
    def clear(self):
        while self.head is not None: # head포인터가 None 아닌동안
            self.remove_first() # 계속 제거한다
        self.current =None
        self.no = 0
    
    def print_current_node(self):
        if self.current is None:
            print("주목 노드가 존재하지않습니다")
        else:
            print("주목노드 메모리값",self.current)
            print("주목노드의 데이터",self.current.data)     
    
    def print(self): # 모든 노드의 데이터값을 출력합니다
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
            
    def __iter__(self):
        return LinkedListIterator(self.head)       
        
    
class LinkedListIterator:
    def __init__(self,head) -> None:
        self.current = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        