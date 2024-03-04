import math

def solution(dp:list,pay:list,target:int):
    dp[0] = 0
    for i in range(len(pay)): # 화폐갯수 순회 
        for j in range(pay[i],target+1): # dp[i] 번째 테이블부터 목표금액까지
            if dp[j-pay[i]] != 10.1:
                dp[j] = min(dp[j] , dp[j-pay[i]] + 1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    pay = list(map(int,input("화폐입력").split()))[:n]
    dp = [10.1 for _ in range(m+1)]
    print("pay : ",pay)
    solution(dp,pay,m)
    
    print("결과출력")
    if dp[m] !=10.1:
        print("최소연산횟수 {}".format(dp[m]))
    else:
        print("화페 연산불가 -1")