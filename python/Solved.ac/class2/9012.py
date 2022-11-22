
line=int(input())

ans_list=list()
for _ in range(line):
    count=0 # ')'의 개수
    data=input();
    stack=list(data) 
    
    if stack[len(stack)-1]=='(': 
        ans_list.append("NO")
        print("NO")
        continue
    
    else:
        while stack: #stack is not empty
            user=stack.pop() # 데이터를 하나꺼냅니다..
            
            if user==")":
                count+=1
                
            else: 
                if count<=0:
                    ans_list.append("NO")
                    print("NO")
                    break
                else:
                    count-=1 #쌍을 맞추었으니 )의 갯수를 줄인다..
                    
        else: #전부 다 닫혔는지 확인
            if count==0:
                ans_list.append("YES")
                print("YES")
            else:
                ans_list.append("NO")
                print("NO")
                
# for i in range(len(ans_list)):
#     print(ans_list[i])