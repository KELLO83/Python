

#선언 5행 4열
mapper = [[50,45,37,32,30],[35,50,40,20,25],[30,30,25,17,28],[27,24,22,15,10]] 
dp = [[-1 for i in range(len(mapper[0]))] for j in range(len(mapper[0]))]
move = [[0,1],[1,0],[0,-1],[-1,0]]

def dp_bruteforce(y,x):
    if dp[y][x] != -1:
        return dp[y][x] # -1이 아니라면 이미 계산됨
                                              
    dp[y][x] = 0
    for i in range(0,4):
        dy = y+move[i][0]
        dx = x+move[i][1]
        if 0 <= dy < 4 and 0 <= dx < 5:
            if[y][x] > mapper[dy][dx]: # 현재 위치의 값이 다음 위치의 값보다 클 때
                dp[y][x] += dp_bruteforce(dy,dx) + 1  # 메모제이션 + 재귀호출 + 1

    return dp[y][x]
print(dp_bruteforce(0,0))