def solution(glasses:list):
    """포도주가 주어졌을떄 최대로많이먹을었을때 포도주의 양은?"""
    """조건 1. 연속으로3잔마시기 불가 조건2. 하나의 포두주잔은 모두 마셔야한다"""
    
    memozation = [0] * len(glasses) # 메모배열 선언
    memozation[0] = glasses[0]
    memozation[1] = glasses[0] + glasses[1]
    for i in range(3,len(glasses)):
        memozation[i] = max(memozation[i-3]+memozation[i-1]+memozation[i] , 
                         memozation[i-2]+memozation[i],memozation[i-1],)
    print()
if __name__ == "__main__":
    glasses = [6,10,13,9,8,1] 
    solution(glasses)