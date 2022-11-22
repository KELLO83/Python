import random

def call_sort(a):
    """ 선택정렬
    0.시작할떄 배열의 0번째 idx는 정렬이 완료되었다고 가정.. 정렬된곳 0번째 정렬안된곳 나머지...
    1. 가장작은원소를 택한다
    2. 기장작은원소를 배열의 앞칸으로 옮긴다
    3. 가장작은원소들을 앞칸으로 옮긴곳은 정렬이 완료된부분이다 
    4. 정렬이안된부분에서 또 작은원소를 찾는다
    5. 정렬이안되부분에서 작은원소를골라서 정렬된부분에서 알맞은idx로삽입한다
    6. 언제까지? -> 정렬이 안된부분이 정렬된부분의 알맞은 idx로 전부 이동할떄까지
    """
    n = len(a) # 배열의 길이를 할당합니다
    cnt=0 # 비교할때마다 증가시킨다
    
    for i in range(n - 1): #배열의 길이만큼 roop를 돌면서...
        min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n): #1~n-1
            cnt+=1
            if a[j] < a[min]:#비교대상이 min보다 작으면 
                min = j#min을 j로 갱신한s다
        a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환 
        # 작은원소를 아직 정렬되지않은부분의 가장작은위치로 이동한다
    print(f"전체 비교횟수 {cnt}")
    print("정렬이 완료된후")
    for i in range(n-1):
        print(a[i],end=' ')
    print()
    
cnt=0                
def qsort(a,left,right): #left 기준점의 왼쪽 right 기준점의 오른쪽
    global cnt 
    pl = left                   #  배열의 맨왼쪽
    pr = right                  #  배열의 맨오른쪽
    x = a[(left + right) // 2]  #  왼쪽과 오른쪽의 중간지점을 구한다

    cnt+=1
    while pl <= pr:    # 오름차순 정렬 pr이 배열의 오른쪽 큰원소가 와야한다 pl 보다 pr이 커야지 정렬완료된상태 즉 -> pr이 클떄까지 기준점을 기준으로 pr 오른쪽 원소들이 클떄까지
        while a[pl] < x: pl += 1 # 정방향 스캔  언제까지? 기준점보다 작을때까지 스캔방향 -------->>>>
        while a[pr] > x: pr -= 1 # 역방향 스캔 언제까지? 기준점보다 클때까지   스캔방향  <<<---------        
        if pl <= pr:  #
            a[pl], a[pr] = a[pr], a[pl] #서로의 자리를 교환한다 
            pl += 1 
            pr -= 1 
        #pl==pr 일떄 완료이지만 알고리즘효율을 위하여 pl>pr일때 종료된다
        # 한번 돌떄마다 if (pl==pr) 을비교한다면 1000번 10000번.. 증가할수록 비효율적,.,.
        
    if left < pr: qsort(a, left, pr) #pr 이 a 0번째 idx보다 오른쪽에 위치시 sort
    if pl < right: qsort(a, pl, right)# pl 이 a 마지막 idx보다 왼쪽에 위치시 sort
    
    

 
if __name__=="__main__":
    data=[random.randint(0,200) for _ in range(21)] #리스트 컴프리핸션 20번roop     
    print("정렬전 {}".format(data))
    print("선택정렬후")
    call_sort(data)
    
    print("=================")
    qdata=[random.randint(0,200) for _ in range(21)]
    qsort(qdata,0,len(qdata)-1)
    print("qsort후 상태",qdata) 
    print("qsort 비교횟수 {}".format(cnt)) #비교횟수이상... 
    print("debug")
