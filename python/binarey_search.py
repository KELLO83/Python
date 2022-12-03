def seqSearch(arr,key):
    start = 0
    end = len(arr)-1
    
    while start<=end:
        middle = (start+end)//2
        if key== arr[middle]:
            return middle
        
        elif key > arr[middle]:
            start = middle+1
        else:
            end = middle-1
            
    return -1 # 실패



data = [7,6,5,8,3,9,1,6]
data.sort()
findData = 0

findData = int(input("찾을값을 입력하세요"))
print("배열 ->",data)

position = seqSearch(data,findData)

if position != -1:
    print(f"찾을데이타 {findData} 는 배열{position}번지 위치합니다")
else:
    print(f"찾을데이터 {findData}를 배열에서 찾지못하였습니다")