from typing import List

# DP 문제 DFS
def solution(mapper:List):
    mapper_size = len(mapper[0]) # 실제인덱스값보다 1크게 저장됨
    memozation = [[-1 for i in range(len(mapper[0]))] for j in range(len(mapper[0]))]
    move = [[0,1],[1,0],[0,-1],[-1,0]]
    current_location = [0,0]
    
    flag = False # 한번검사 ---> True 두번검사
    for i in range(len(mapper_size)-1,0,-1): #
        target_index = mapper[i] 
        if flag == False: #한번검사
            pass

if __name__ == "__main__":
    mapper = [[50,45,37,32,30],[35,50,40,20,25],[30,30,25,17,28],[27,24,22,15,10]]
    solution(mapper)