#DFS 
#G=(v,E)
#stack

        
class graph(object):
    def __init__(self,vertex):
        self.vertex=vertex
        self.adj_list=[ []  for _ in range(self.vertex)]
        self.visitde=[False for _ in range(self.vertex)]
        print(self.adj_list)
        
    def add_adge(self,vertex_1,vertex_2):
        Maximum=len(self.adj_list)
        print(Maximum)
        print(type(Maximum))
        if vertex_1>=Maximum or vertex_2>=Maximum:
            print("vertex_1 vertex2 의 범위가 잘못되었습니다")
            return False
        
        for i in self.adj_list[vertex_1]:
            if self.adj_list[vertex_1]==vertex_2:
                print("중복된 값")
                return False
        self.adj_list[vertex_1].append(vertex_2)
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
        stack=list()
        self.visitde[start]=True
        current_node=start
        print("{} visited".format(start))
        stack.append(start)
        
        
                    
                
        
if __name__=="__main__":
    a=graph(4)
    a.add_adge(0,1)
    a.add_adge(0,2)
    a.add_adge(2,3)
    a.add_adge(3,2)
    a.detail()
    
    