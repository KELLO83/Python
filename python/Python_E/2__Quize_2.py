#세정수를 입력받은후 가장큰숫자를 출력하라

Max=0
for _ in range(3):
    count=1
    n1=int(input("{}번째 정수를 입력하세요".format(count)))
    if Max<n1:
        Max=n1
    count+=1

print("가장 큰수는 %d입니다"%Max)    
    