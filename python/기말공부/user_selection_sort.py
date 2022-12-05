def sort(a):
    for i in range(len(a)-1):
        min = i # 아직 정렬안된곳의 시작지점을 일단 가장작다고 가정합니다
        for j in range(i+1,len(a)-1): #정렬이안된부분의+1 부터 시작해서
            if a[j] < a[min]:  # 스캔방향의 제일작은값을 찾아서
                min = j # min값을 가지는 idx를 가리킵니다
        a[i] , a[min] = a[min] , a[i] # 이후 정렬이안된부분의 시작지점과 자리교환을 진행합니다
    
        
    print("정렬완료",a)
    
if __name__ =="__main__":
    data = [7,6,5,8,3,5,9,1,6]
        
        