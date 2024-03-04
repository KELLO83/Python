#두정수 A와 B를 입력받은다음 A+B를 출력하는 프로그램을 작성하시오
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break
        

""" 문제의 핵심 어떨때 종료될까??? ->범위가 아웃이건
buffer=collections.deque() 
while True:
    # print("두 정수 A와 B를 입력받습니다")
    user_data=list(map(int,input().s5plit()))
    try:
        if user_data[0]>0 and user_data[1]>0 and user_data[0]<10 and user_data[1]<10:
            buffer.append(user_data)
    except:
        break
while buffer:
    out=buffer.popleft()
    print(out[0]+out[1])
"""

""" ???????????? 범위가있음에도 불구하고 에러발생
buffer=collections.deque() 
while True:
    try:
        a,b=map(int,input().split())
        if a>0 and a<10 and b>0 and b<10:
            raise ValueError
        print(a+b)
    except ValueError: #out of range
        break        
    except: #map error
        break

"""