#stk를 이용한 recur구현


import collections

def recur(n):
    s=collections.deque()
    while True:
        if n>0:
            s.append(n)
            n=n-1
            continue
        if s:
            n=s.pop()
            print(n)
            n=n-2
            continue
        break
    

            
    