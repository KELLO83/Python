def solution(dp:list,mapper:list,row,colum):
    row_size = row
    col_size = colum
    for row in range(row):
        for colum in range(1,colum):
            if 0 <= row < row_size and  0 < colum < col_size: # 정상범위
                if row ==0 : # 첫번째 행이라면  예외조건  윗대각 접근 불가
                    dp[row][colum] = mapper[row][colum] + max(dp[row][colum-1],dp[row + 1][colum-1])
                elif row == row_size -1 : # 마지막행이라면 아랫대각 접근불가
                    dp[row][colum] = mapper[row][colum] + max(dp[row][colum-1], dp[row - 1][colum-1]) 
                else: # 에외사항없을떄
                    dp[row][colum] = mapper[row][colum] + max(dp[row+1][colum-1],dp[row][colum-1],dp[row-1][colum-1])                          
    return dp
                
                 
if __name__ == "__main__":
    row , colum = map(int,input("행 열을 입력하세요").split()) # 3행 4열
    mapper = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]
    dp = [[0 for _ in range(colum)] for _ in range(row)]
    for i in range(row):
        dp[i][0] = mapper[i][0]
    print("들어가기전 dp 맵 : ",dp)
    solution(dp,mapper,row,colum)
    print("dp : ",dp)