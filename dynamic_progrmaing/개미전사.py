

def solution(store:list,dp:list)->int:
    """바텀업 방식"""
    dp[0] = store[0]
    dp[1] = max(store[1],dp[0])
    for i in range(2,len(store)):
        print("DP테이블 : ",dp) 
        if dp[i] != -1: # 메모됨 이미한번계산함
            pass
        else: #아직 계산되지않음 게산을 해야함 게산은 현재위치 + 전전위치 dp값
           dp[i] = store[i] + dp[i-2] 
        print()
    
    print("DP테이블 : ",dp)
    answer = max(dp)
    return answer
            


if __name__ == '__main__':
    n = int(input())
    store = list(map(int,input().split()))[:n]
    dp = [-1 for i in range(n)]
    print("store : ",store)
    print("dp",dp)
    print(solution(store,dp))