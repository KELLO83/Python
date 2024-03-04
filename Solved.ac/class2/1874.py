stack=list()
operator_DB=list()

# https://data-flower.tistory.com/98
line=int(input())
index=1 #스택의 최댓값

for _ in range(line):
    user=int(input())
    while index<=user:
        stack.append(index)
        operator_DB.append("+")
        index+=1
        
    if stack[len(stack)-1]==user:
        stack.pop()
        operator_DB.append("-")
    else:
        operator_DB.append("NO")


if operator_DB.count("NO")>=1:
    print("NO")
else:
    for i in range(len(operator_DB)):
        print(operator_DB[i])