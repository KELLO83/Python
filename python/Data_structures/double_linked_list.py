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
            x_node.next=a_node
            b_node.next=temp
            ap=x_node
            bn=xn
            xn.previous=b_node
            # ap.next=bn
            # b_node.next=x_node.next
            # x_node.next=a_node
            
  
            print("splice")
            
    def Move_After(self,a,x): #노드 a를 x다음으로 이동한다
        self.splice(a,a)
        
            
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
    link.splice(1, 3, 4) #처음시작 0번을 떄는것을 불가 수정필요...
    print("\n")
    link.detail()


    
    