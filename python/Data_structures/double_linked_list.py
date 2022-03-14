#double linked list
#Node
#circle list


class Node():
    
    def __init__(self,key):
        self.key=key
        self.next=None
        self.previous=None
        self.node_number=None
    def __repr__(self):
        return self.key
    
class double_linked_list():
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
            new_node.node_number=0
        else:
            new_node.next=self.head
            new_node.node_number=0
            self.head=new_node
            new_node.next.previous=new_node
            self.size+=1
            travel=new_node
            
            for _ in range(len(self)-1):
                travel.next.node_number+=1
                travel=travel.next    
            node=self.head
            node.previous=travel    
            node.previous.next=self.head
            
    def delete_Node(self,Node_number):
        search=self.head
        
        while search.node_number!=Node_number:
            search=search.next
            
        print("delte target {} delete Node_key {}".format(search.node_number,search.key))
           
   
        
    def detail(self):
        travel=self.head
        for _ in range(len(self)-1):
            print("{} Node Node_data {}".format(travel.node_number,travel.key))
            travel=travel.next
            
        print("{} Node Node_data {}".format(travel.node_number,travel.key))
        print("\n")
    
    
    def research_back(self,Node_number):
        if len(self)==0:
            print("노드가 존재하지않습니다")
            return None
        else:
            find=self.head
            while find.node_number!=Node_number:
                find=find.next
            try:
                print(find.previous.key)
            except:
                print("None previous Node")
                return None
    def splice(self,a,b,x): #세개의 노드 a b x #조건 a노드는 head노드가 될수없다 즉 첫번째 노드는 불가하며 조건 a>=b노드이다
            v=self.head
            Node_find=0
            for _ in range(len(self)-1):
                if Node_find==a:
                    a_node=v
                elif Node_find==b:
                    b_node=v 
                elif Node_find==x:
                    x_node=v
                v=v.next
                Node_find+=1
            
            ap=a_node.previous
            bn=b_node.next
            xn=x_node.next
            
            ap.next=bn
            bn.previous=ap
            temp=x_node.next
            x_node.next=a_node #문제발생지점 >>>
            b_node.next=temp
            ap=x_node
            bn=xn
            xn.previous=b_node
            x_node.next.previous=x_node #해결
            # ap.next=bn
            # b_node.next=x_node.next
            # x_node.next=a_node
            
            print("splice")
  
    def circle_check(self):
        find=self.head
        count=0
        while find.next!=None:
            print("{} Node Node_data {}".format(find.node_number,find.key))
            count+=1
            find=find.next
            if count==20:
                break
        
        print("circle check end")
        print("\n") 
    def circle_check_back(self):
        find=self.head
        count=0
        while find.previous!=None:
            print("{} Node Node_data {}".format(find.node_number,find.key))  
            count+=1
            find=find.previous
            if count==20:
                break
        print("circle back check end")    
        print("\n")
    def move_after(self,move_node,standard_node):
        find=self.head
        find_standard=self.head
        for _ in range(move_node):
            find=find.next
        for _ in range(standard_node):
            find_standard=find_standard.next
        print("move_node {} move_key {}".format(find.node_number,find.key))
        print("standard_node {} standar key {} ".format(find_standard.node_number,find_standard.key))
        fn=find.next
        fp=find.previous
        fsn=find_standard.next
        fp.next=fn#옮기고자하는 노드의 그전노드의 다음을 옮기고자하느 노드의 그다음노드랑 연결시킨다
        fn.previous=fp#위 사항의 백연결
        find_standard.next=find #옮기는 노드를 내가 정한기준점의 노드 그다음에다가  갖다놓는다
        find.previous=find_standard #위사항의 백연결
        find.next=fsn
        self.detail()
        
    def move_before(self,move_node,standard_node):
        find=self.head
        find_standard=self.head
        for _ in range(move_node):
            find=find.next
        for _ in range(standard_node):
            find_standard=find_standard.next    
        
        print("move node {} move key {}".format(find.node_number,find.key))
        print("standard_node {} standard key {}".format(find_standard.node_number,find.key))
        fp=find.previous #1번노드
        fn=find.next #3번노드
        fsn=find_standard.next #6번노드
        fsp=find_standard.previous#4번노드
        fp.next=fn
        fn.previous=fp
        fsp.next=find
        find.previous=fsp
        find_standard.previous=find
        find.next=find_standard
        
        
        
        
  
        
        
if __name__=="__main__":
    link=double_linked_list()
    
    link.pushFront(5)
    link.pushFront(100)
    link.pushFront(1000)
    link.pushFront(2000)
    link.pushFront(3000)
    link.pushFront(4000)
    link.pushFront(5000)
    link.delete_Node(3)
    link.detail()
    # link.splice(0, 3, 4) #처음시작 0번을 떄는것을 불가 수정필요... 수정완료
    # link.detail()
    # link.circle_check()
    # link.circle_check_back() #BACK 이상 해결
    # link.move_after(2, 4)
    link.move_before(0, 5)
    link.circle_check()
    link.circle_check_back()
    
    


    
    