class Node:
    def __init__(self, data=None , prev=None, next=None):
        self.data = data # 해당노드에 데이터
        self.prev = prev # 앞쪽노드포인터
        self.next = next # 뒤쪽노드 포인터
        
        
class DoubleLinkedList:
    # 더블링크드리스트는 더미노드를 생성후 헤드노드가 더미노드를 지칭합니다
    def __init__(self) -> None:
        self.head = self.current = Node() # 헤드는 일단 더미노드
        self.no = 0
        
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.head.next is self.head # 헤드노드의 NEXT가 자기자신이라면 노드존재x
    
    def search(self,data):
        cnt = 0 
        ptr =self.head.next # 더미노드의 다음이 실질적인 노드이다
        while ptr is not self.head: # 실질노드부터해서 순회하여 더미노드까지 오는동안 검색한다
            if data ==  ptr.data:
                self.current = ptr 
                return cnt
            cnt +=1
            ptr = ptr.next # 주목노드의NEXT로 주목노드를 이동한다
        return -1 
    
    def __contains__(self,data):
        return self.search(data) >=0
    
    def print_current_node(self):
        if self.is_empty():
            print("주목노드가 존재하지않습니다")
        else:
            print("주목노드의 메모리주소",self.current)
            print(self.current.data)  #주목노드의 데이터값 출력
            
    def print(self):
        ptr = self.head.next  # 실질노드부터 시작합니다
        while ptr is not self.head: # 더미노드까지 오는동안
            print("주소와 데이터값",ptr,ptr.data)
            ptr = ptr.next
            
    def print_reverse(self):
        ptr = self.head.prev # 실지노드의 꼬리부터 시작합니다
        while ptr is not self.head:
            print("주소와 데이터값",ptr,self,ptr)
            ptr = ptr.prev
    
    def next(self):
        if self.is_empty():
            return False # 이동불가
        self.current = self.current.next
        return True
    
    def prev(self):
        if self.is_empty():
            return False # 이동불가
        
    def add(self,data):
        """ 주목노드 뒤에 노드 삽입"""
        node = Node(data,self.current,self.current.next) # 삽입한다
        self.current.next.prev = node # 주목노드의 다음노드의 이전속성을 새로만든NODE를 삽입한다
        self.current.next = node   #주목노드의 next속성을 새로만든NODE를 삽입한다
        self.current = node #주목노드이 이동
        self.no += 1
        
    def add_first(self,data):
        self.current = self.head # 헤드가 가리키고있는것은 일단 더미노드
        self.add(data)
        
    def add_last(self,data):
        self.current = self.head.prev # 주목노드는 더미노드의 꼬리부터시작한다
        self.add(data)
    
    def remove_current_node(self) :
        """ 주목노드 삭제"""
        if not self.is_empty():
            self.current.prev.next = self.current.next # 주목노드이 이전의 next속석을 주목노드의next로 연결한다
            self.current.next.prev = self.current.prev # next노드의 이전속성을 주목노드의 이전으로 연결한다
            self.current = self.current.prev # 주목노드 전으로 이동하며 링크절단
            self.no -=1
            if self.current is self.head: #주목노드가 헤드노드이라면
                self.current = self.head.next # 주목노드를 헤드노드의 다음인 실질노드로 이동한다
                
    def remove(self,p:Node):
        ptr = self.head.next
        
        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next
            
    def remove_first(self):
        self.current =self.head.next # 처음노드를 삭제하며 실질노드로 주목점을 잡는다
        self.remove_current_node()
        
    def remove_last(self):
        self.current = self.head.prev # 꼬리노드로 이동한다 head는 더미노드를 가리키고있다
        self.remove_current_node()
        
    def clear(self):
        while not self.is_empty():
            self.remove_first()
        self.no = 0
        
    def __iter__(self):
        pass
    
class DoubleLinkedListIterator:
    """ 반복자 정방향"""
    def __init__(self,head) -> None:
        self.head = head
        self.current = head.next
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        
class DoubleLinkedListReverseIterator:
    """ 반복자 역방향"""
    def __init__(self,head) -> None:
        self.head = head
        self.current = self.head.prev
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
        