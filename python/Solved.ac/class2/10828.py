import sys
line=int(input())

# Stack FILO 구조 

"""
push는 출력하지않는다
top -> Stk의 상단을 조회한다
size -> Stk의 사이즈를 조회하다
empty -> Stk가 empty인지 확인한다  empty이면 1반환 아니면 0반환
pop -> Stk 상단의 데이터를 삭제하며 반환한다


"""
stack=list()
for i in range(line):
        user=sys.stdin.readline().split()
        
        command=user[0]
        if command=='push':
            stack.append(int(user[1]))
            
        elif command=='pop':
            try:
                data=stack.pop()
                print(data)
            except:
                print("-1")
            
        elif command=="size":
            print(len(stack))
            
        elif command=='empty':
            if len(stack)==0:
                print("1")
            else:
                print("0")
                
        elif command=="top":
            if len(stack)!=0:
                print(stack[len(stack)-1])
            else:
                print("-1")