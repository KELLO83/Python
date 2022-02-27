#travel
#G=(v,E)
#stack
import collections
import random
import time

class graph(object):
    def __init__(self,vertex):
        self.vertex=int(vertex)
        self.adj_list=[ []  for _ in range(self.vertex)]
        self.visitde=[False for _ in range(self.vertex)]
        self.sequence=list()
        print(self.adj_list)
        
    def add_adge(self,vertex_1,vertex_2):
        Maximum=len(self.adj_list)
        if vertex_1>=Maximum or vertex_2>=Maximum:
            print("vertex_1 vertex2 의 범위가 잘못되었습니다")
            return False
        
        for i in self.adj_list[vertex_1]:
            if self.adj_list[vertex_1]==vertex_2:
                print("중복된 값")
                return False
        self.adj_list[vertex_1].append(vertex_2)
        
        print("generate edge {} to {}".format(vertex_1,vertex_2))

    def add_vertex(self,count):
        temp=[[] for _ in range(count)]
        self.adj_list.extend(temp)
        print("정점 {}개 추가완료".format(count))
    
    def delete_edge(self,standard,find_node):
        self.adj_list[standard].remove(find_node)
        print("delete edge {} to {}".format(standard,find_node))
        
    def delete_vertex(self,standard):
        del self.adj_list[standard]
        for i in self.adj_list:
            for j in i:
                if j==standard:
                    i.remove(standard)
                
    def is_linked(self,standard,find_node):
        for i in self.adj_list[standard]:
            if i==find_node:
                print("linked {} to {}".format(standard,find_node))
                return True
        else:
            print("not linked {} to {}".format(standard,find_node))
            return False    
        
    def detail(self):
        print("adj_list={}\n".format(self.adj_list))

    def dfs(self,start): 
        #재귀호출을 이용한 dfs구현 함수호출이 스택구조 쌓이게된다 재귀함수호출시 현재 실행줄인 함수를 잠시 스택에 보류하고 새로운 함수를 실행한다 이후 새로운함수가 종료될시
        #함수 호출 스택상단에 존재하는 함수를 진행한다
        print("visited {}".format(start))
        self.visitde[start]=True
        self.sequence.append(start)       
        adj_v=self.adj_list[start]
        for u in adj_v:
            if not self.visitde[u]:
                self.dfs(u)
        
                
    def sequence_node(self):
        for i in self.sequence:
            print("{}->".format(i),end='')   
        
        print("finsih")   
                
        
if __name__=="__main__":
    vertex_count=input("정점의 갯수 입력")
    make_edge=input("생성할 엣지의 갯수")
    a=graph(vertex_count)
    random.seed(time)
    
    for i in range(int(make_edge)):
        n1=random.randrange(0,int(vertex_count))
        n2=random.randrange(0,int(vertex_count))
        insepct=a.adj_list[n1]
        overlap=False
        
        for i in insepct:
            if i==n2:
                print("이미존재하는 엣지 {} to {}".format(n1,n2))
                overlap=True
        
        if overlap==False:
            a.add_adge(n1, n2)

        else:
            pass
            
        

    a.detail()
    a.dfs(0)
    a.sequence_node()
    
    
    

    
