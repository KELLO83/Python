import collections
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
buffer=collections.deque()
while True:
    print("두정수 입력")
    data=list(map(int,input().split()))
    if data[0]==0 and data[1]==0: #둘다 0을 입력받으면..
        break #탈출
    buffer.append(data)
while buffer:
    out=buffer.popleft()
    print(out[0]+out[1])
        
    