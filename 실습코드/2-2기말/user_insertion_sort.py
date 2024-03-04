def sort(a):
    
    for i in range(1,len(a)-1):
        j = i # j는 위치포인터 1부터시작한다
        tmp = a[i] # 위치포인터 값을 tmp에저장한다
        while j > 0 and a[j-1] > tmp: # 위치포인터에서 역방향으로 진행한다
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
        
    print("정렬완료",a)
        
        
if __name__ == "__main__":
    data = [7,6,5,8,3,5,9,1,6]
    sort(data)