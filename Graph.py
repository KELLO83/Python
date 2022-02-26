import collections

class Graph:
    def __init__(self, vertex_num):
        self.adj_list=[] #정점의 인접 정점
        self.vtx_num=0 #정점의개수
        self.vtx_arr=[] #정점의 존재여부

        if vertex_num:
            self.vtx_num=vertex_num
            self.vtx_arr=[True for _ in range(self.vtx_num)]
            self.adj_list=[[] for _ in range(self.vtx_num)]
            
            print("00")
    def is_empty(self):
        if self.vtx_num==0:
            return False
        else: 
            return True
        
    def add_vertex(self):
        self.vtx_arr.append(True)
        self.adj_list.append([])
        self.vtx_num+=1
        
    def delete_vertex(self,del_vtx):
        self.adj_list.pop(del_vtx)
        self.vtx_arr.pop(del_vtx)
        self.vtx_num-=1
        for i in self.adj_list:
            try:
                i.remove(del_vtx)
            except:
                pass        
    
    def add_edge(self,data_1,data_2): #무향그래프
        if len(self.vtx_arr)-1>=(data_1) and len(self.vtx_arr)-1>=(data_2):
            self.adj_list[data_1].append(data_2)
            self.adj_list[data_2].append(data_1)
        else:
            print("data_1과 data_2의 범위가 잘못되었습니다1")
            return False
    
        
    
        
    def detail(self):
        print("self.adj_list={}\nself.vtx_num={}\nself.vtx_arr={}\n".format(self.adj_list,self.vtx_num,self.vtx_arr))
        
        
if __name__=="__main__":

    a=Graph(4)
    a.detail()
    a.add_edge(3, 2)
    a.detail()
    a.add_edge(1,3)
    a.detail()
    a.delete_vertex(1)
    a.detail()


















