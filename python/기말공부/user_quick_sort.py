def sort(n,left,right):
    start = left
    end = right
    pivot = (start + end) // 2
    
    while start<=end:
        while n[start]<n[pivot]:
            start +=1
        while n[end] > n[pivot]:
            end -=1
        if start <=end:
            n[start] , n[end] = n[end] , n[start]
            start+=1
            end-=1
            
        if left < end:
            sort (n,left,end)
        if right > start:
            sort(n,start,right)
    
    

if __name__ == "__main__":
    data = [7,6,5,8,3,5,9,1,6]    
    print("정렬전",data)
    sort(data,0,len(data)-1)            
    print("정렬완료",data)    