#1000이하의 소수를 나열하는프로글매
# 소소=자신과 1이외의 정수로 나누어떨어지지않는 정수


def orgin():
    counter=0

    for i in range(2,1001):
        for j in range(2,i):
            counter+=1
            if i%j==0:
                break
        else:
            print(i)

    print(f"나눗셈을 실행한횟수{counter}")        
    
    
def improve_first():
    counter=0 #나눗셈을 시도한횟수
    ptr=0 #이미찾은 소수의 갯수
    prime=[None]*500 #소수를 저장하는 배열
    prime[ptr]=2 #default값 소수2로설정
    ptr+=1 #한개증가
    #짝수는 전부 소수가아님
    for n in range(3,1001,2): #홀수만을대상으로 설정
        for i in range(1,ptr): #ragne범위 1부터 이미찾은 소수의 갯수까지
            counter+=1
            if n%prime[i]==0:
                break #소수가아니므로 종료합니다
        else:
            prime[ptr]=n #새로운소수를 배열에 저장
            ptr+=1 #소수갯수 증가
            
def imporver_second():
    counter=0 #나눗셈을 실행한횟수
    ptr=0 #소소의 갯수
    prime=[None]*500 #소루를 저장하는 arr
    
    prime[ptr]=2 #default값 2추가
    ptr+=1 #소수갯수 증가
      
    prime[ptr]=3 #default 값 3추가
    ptr+=1 #소수갯수 증가
    
    for n in range(5,1001,2): #4는소수가아니므로 5부터시작하면 홀수단위만 체크한다
        i=1
        while prime[i]*prime[i]<=n: #
            counter+=2
            if n%prime[i]==0:
                break
            i+=1
        else:
            prime[ptr]=n
            ptr+=1
            counter+=1
            
    for i in range(ptr):
        print(prime[i])
    print("곱셈과 나눗셈을 실행한 횟수{}".format(counter))            
         

if __name__=="__main__":
    orgin()
    improve_first()
    imporver_second()