def sort(a):
    start = 0 # 시작 위치포인터
    end = len(a)-1 #마지막 위치포인터
    point = end # 자리교환을 마지막으로 마친곳
    while start < end: # start == end 일경우 정렬이 완료되었다
        for j in range(end,start,-1): # 역방향 진행
            if a[j] < a[j-1]: # 앞쪽이 값이 더클경우 뒤쪽으로 보낸다
                a[j] , a[j-1] = a[j-1] ,a[j]
                point = j 
            start = point  # last는 위에 for문을 실행하면서 마지막으로 원소를 바꾼자리를 기억한다
            
        for i in range(start,end): #정방향 진행
            if a[i] > a[i+1]: # # 뒤쪽이 작은원소라면 앞쪽으로 이동한다
                a[i] , a[i+1] = a[i+1] ,a[i]
                point = i
            end = point
    # point의역할 정/역방향으로 진행하며 맨끝은 정렬이완료된다 그러므로 start end 위치포인터를 갱신시켜준다
    print("정렬완료",data)    



if __name__ == "__main__":
    data = [7,6,5,8,3,5,9,1,6]
    sort(data)