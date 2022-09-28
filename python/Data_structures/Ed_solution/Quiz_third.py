counter=0

for n in range(2,7): # 2 3 4 5 6
    for i in range(2,n):
        counter+=i
        if n%i==0:
            break 
        else: 
            print(n)
            print("나눗셈을 실행한횟수 {}".format(counter))
            print()
            

"""
n=2일때 x 

n=3일떄 count=2   // n=3 out 2

n=4일떄 count=4 

n=5일때 count=6 //n=5 out 6 
count=9// n=5 out 9 
count=13// n=5 out 13

n=6일떄 count=15  종료

n%i==0이되는경우 이중for문을 종료한다 또한 n%i==false 일때마다 
즉 n이 i의 약수가 아닐때마다 print를하여 현재 n값과 나눗셈의 결과를 계속 출력한다



"""