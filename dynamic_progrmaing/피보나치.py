def solution(dp:list,target:int):
    dp[0] = 1
    dp[1] = 1
    if target == 1:
        return dp[1]
    
    for i in range(2,target+1):
        dp[i] = dp[i-2] + dp[i-1]



if __name__ == "__main__":
    target = int(input("몇번째 피보나치 수열을 구할까요?"))
    dp = [0 for i in range(target+1)]
    solution(dp,target)
    
    print("{}번째 피보나치 수열은 {}입니다".format(target,dp[target]))