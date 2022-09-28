count=0

for n in range(2,7):
    for i in range(2,n):
        count+=i
        if n%i==0: 
            continue #break=>continue 변환
    else:
        print(n)
        print("나눗셈을 실행한횟수 {}".format(count))
        print()
        

"""
cotinue문으로 인해서 break와 달리 약수여도 이중for문을 끝까지 진행한다 결국 모든n에대해서 나눗셈결과를 출력한다

n=2 일떄 n=2 // n=2 out=0

n=3일떄 count=>2 // n=3 out=2

n=4일때 count=>4 count=>7 //n=4 out 7

n=5일떄 count=>9 count=>12 count=> 16 // n=5 out 16

n=6알때 2+3+4+5=14  count=>30 //n=6 out 30



"""
        