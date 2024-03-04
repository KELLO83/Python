# Linked list
#Node 는 key값과 link로 구성되어진다
#단뱡향 연결리스트

class Node(object):
    def __init__(self,key=None):
        self.key=key
        self.next=None
    # def __str__(self):
    #     return str(self.key)
    # def __repr__(self):
    #     return str(self.key)
    
class SinglyLinkedList():
    def __init__(self):
        self.head=None
        self.size=0
        
    def __len__(self):
        return self.size      
    
    def pushFront(self,key):
        new_node=Node(key)
        
        if len(self)==0: #__len__(self)
            print("최초의 노드")
            self.head=new_node
            self.size+=1
        
        else:
            new_node.next=self.head
            self.head=new_node
            self.size+=1
            
    def pushback(self,key):
        new_node=Node(key)
        
        if len(self)==0:
            print("최초의 노드")
            self.head=new_node
            self.size+=1
        else:
            tail=self.head
            
            while tail.next!=None:
                tail=tail.next    
                 
        tail.next=new_node
        self.size+=1
    
    def travel(self):
        travel=self.head
        
        if travel.next==None:
            print("head 노드만 존재합니다")
            print("Node_count {}".format(1))
            
            return 0
        Node_count=1
            
        while travel.next!=None:
            print("Node_count={} Node_data{} ".format(Node_count,travel.key))
            travel=travel.next
            Node_count+=1
            
        print("Node_count={} Node_data={} ".format(Node_count,travel.key))
        print("travle 종료\n")
    def popfront(self):

        if len(self)==0:
            print("현재 존재하는 노드가 없습니다")
            return None
        
        else:
            x=self.head
            key=x.key
            self.head=x.next
            self.size-=1
            del x          #메모리 unlock
            return key   
    
    def popback(self):
        
        if len(self)==0:
            print("현재 존재하는 노드가 없습니다")
            return None
        
        tail=self.head
        Previous=None # tail의 전노드 
        
        while tail.next!=None:
            Previous=tail
            tail=tail.next
        
        if len(self)==1:
            self.head=None
            print("모든 노드를 지웠습니다 현재 존재하는 노드가 존재하지않습니다")
            self.size-=1
            return None
        
        else:
            self.size=None
            Previous.next=None
            key=tail.key
            del tail
         
            return key
    
    def delete_node(self,Node_number):
        
        if len(self)==0:
            print("현재 존재하는 노드가없습니다")   
        
        find=self.head
        Previous=None
        
        for _ in range(int(Node_number)):
            Previous=find
            find=find.next
        
        self.size-=1
        Previous.next=find.next
        key=find.key
        del find
        
        return key
     
    def create_node(self,key,insert_Node_number):
        new_node=Node(key)
        find=self.head
        previous=None
        
        for _ in range(int(insert_Node_number)):
            previous=find
            find=find.next
            
        self.size+=1
        new_node.next=find
        previous.next=new_node
        
    def search(self,key): 
        
        travel=self.head
        while travel!=None:
            if travel.key==key:
                print("find key={}".format(travel.key))
                return key
            travel=travel.next
        return None
    
    def __iterator__(self): #for+in+list =generate
        v=self.head
        
        while v!=None:
            yield v # generate yield 있는함수 yiled=return이랑 비슷
            v=v.next
        
        
                   
if __name__=="__main__":
    L=SinglyLinkedList()
    L.pushFront(-1)
    L.pushback(4)
    L.pushFront(5)
    L.travel()
    L.delete_node(1)
    L.travel()
    L.pushback(100)
    L.pushback(200)
    L.delete_node(2)
    L.travel()
    L.create_node(1000, 1)
    L.travel()
    L.search(4)
    L.__iterator__()
    
    for x in L.__iterator__():
        print(x)
    
    
    
