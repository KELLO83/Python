def sort(a):
    n = len(a)
    h = n//2  # 원소들간의 간격
    while h>0: # 1정렬까지수행
        for i in range(h,n): # h부터시작해서 배열의끝까지
            target = i - h 
            taget_value = a[i] # h간격의 처음시작점의 값
            
            while target >=0 and a[target] > taget_value:
                a[target+h] = a[target]
                target -=h
                a[target + h] = taget_value
        h//=2
        
    print("정렬완료",a)
    
if __name__ =="__main__":
    data = [7,6,5,8,3,5,9,1,6]
    sort(data)