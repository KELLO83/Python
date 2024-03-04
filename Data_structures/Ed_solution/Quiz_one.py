counter=0

for n in range(2,7): # 2 3 4 5 6
    for i in range(2,n):
        counter+=i
        if n%i==0:
            break #break가 걸릴시 else문을 찍지않는다
    else: #else문 이중for문이완전히끝날때 out 또는 이중for문에 들어가지않을떄 
        print(n)
        print("나눗셈을 실행한횟수 {}".format(counter))
        print()
        
        
        
"""
n=2일때 변화없음 out 0 n=2
 
n=3 일떄 count=>2 out 2 n=3

n=4일떄 count=>4  터미널 출력 x

n=5일떄  count=>6 count=>9 count=>13 out 13 n=5

n=6일떄  count=>15 break 종료 터미널 출력 x

n%i==0 으로인해서 n이 i 의 약수일떄 이중for문의 진행을 종료하며 else를 찍지않는다



"""