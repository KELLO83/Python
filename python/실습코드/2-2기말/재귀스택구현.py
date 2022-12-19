# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)
import collections
def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = collections.deque()

    while True:
        if n > 0:
            s.append(n)         # n 값을 푸시
            n = n - 1
            continue          
        
        if len(s)!=0:  # 스택에 비어있지않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2   
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)