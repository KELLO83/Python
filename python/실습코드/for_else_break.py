count=0
for n in range(2,7):
    for i in range(2,n):
        print("for실행=> i:{} n:{}".format(i,n))
        count+=1
        if n%i==0:
            break
        print("for실행 (break후)=> i:{} n:{}".format(i,n))
        print("------------------------")
    else:
        print("else 실행=> i:{} n:{}".format(i,n))
        print(n)
        print("나눗셈실행횟수 : {}".format(count))
        print("======================")