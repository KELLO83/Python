def solution(dp:list,target:int):
    dp[1] = 1
    dp[2] = 3
    for i in range(3,target+1):
        dp[i] = ( dp[i-2] * 2 + dp[i-1] * 1 ) % 796796     

if __name__ == "__main__":
    target = int(input("타일을 입력하세요"))
    print("{} * 2 타일을 채우는 모든방법의 수를 출력합니다".format(target))
    dp = [0 for i in range(target+1)]
    solution(dp,target)    
    print('dp : ',dp)
    print("결과 : {}".format(dp[target]))