def solution(number:int,dp:list):
    dp[0] = 0
    for i in range(2,len(number)+1):
        dp[i] = dp[i-1] + 1 # 26일때 25일떄 호출횟수 + 1
        if i % 2 == 0: 
            dp[i] = min(dp[i//2]+1 ,dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1 , dp[i])
        if i % 5 == 0:
            dp[i] == min(dp[i//5]+1 , dp[i])
    return dp[number]
if __name__ == "__main__":
    number = int(input("숫자를 입력하세요"))
    dp = [-1 for i in range(number)]
    print(solution(number,dp))