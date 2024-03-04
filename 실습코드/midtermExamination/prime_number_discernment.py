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
        else:# else를 출력한다는것은 n을 지금까지 저장된 소수로 모두 나누었더니 n%i!=0 즉 n이 소수라는것이다
            prime[ptr]=n #새로운소수를 배열에 저장
            ptr+=1 #소수갯수 증가
"""
3 5 7 9 11 13 홀수만 판별하면서
2를 일단 소수에저장하고 
3을 소수판펼할때 소수버퍼에 2만저장되어있으므로 소수카운트만큼 3을 for검사를 돌림

만약 7를판별할떄는 소수버퍼에 2,3,5가저장되어있으므로 소수카운터는 3이다 그럼 for i in range(1,3) 세번 검사로써 if n%소수리스트[i] 로 7%2 7%3 7%5 가 0인지 판별한다 
만약 0일경우는 소수가아니다 그러나 모든mod연산을통한 검사가 0이아닐경우는 소수이므로 소수버퍼에 n을추가하며 소수갯수를 한개증가시킨다
"""
            
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
        while prime[i]*prime[i]<=n: #소수의 제곱근 어떤수 x는 n*m으로 된다 이떄 중복검사를 하지않기위해서
            # n*m m*n 이 중간지점을 구한다
            counter+=2 #중복검사이므로 +1이아닌 +2를한다
            if n%prime[i]==0: #나누어떨어지면 소수가아니다
                break #증가된 n for증가
            i+=1
        else: #N을 전부 저장된소수로 나누었을떄 !=0이라면 소수이다 
            prime[ptr]=n #소수버퍼에 소수추가
            ptr+=1 #소수갯수 증가
            counter+=1 #나눗셈횟수 증가
            
    for i in range(ptr):
        print(prime[i])
        print("곱셈과 나눗셈을 실행한 횟수{}".format(counter))            
""" 17이 소수인지 판별한다
이미저장된 소수 버퍼 2 3 5 7 11 13 
소수카운터 6
1*17
2*8.5
3*5.66
5*3.4 =>N이 5가될떄 M보다 커진다 그이후는 중복검사할필요없다 즉 N*M이 N의 제곱보다 작거나같을떄까만 roop
7*2.24
11*1.54
13*1.07
"""            
def user_improve():
    count=0
    buffer=list()
    buffer_count=0
    buffer.append(2)
    buffer_count+=1
    buffer.append(3)
    buffer_count+=1
    
    for i in range(5,51,2):
        for j in range(buffer_count):
            count+=1
            if i%buffer[j]==0:
                break #소수가아니다 그다음 숫자를검사한다
        else : #for문을 다돌았다면 그수는 소수이다
            print(i,end=" ") 
            buffer.append(i)
            buffer_count+=1
        
        
    print()
    
def user_sqrt_imporve():
    count=0
    buffer=list()
    buffer_count=0
    buffer.append(2)
    buffer.append(3)
    buffer_count+=2

    for i in range(5,51,2):
        j=0
        while buffer[j]*buffer[j]<=i:
            count+=2
            if i%buffer[j]==0:
                break #소수가아니다
            j+=1
        
        else:
            print(i,end=" ")
            buffer.append(i)
            buffer_count+=1
            
        


        
if __name__=="__main__":
    # orgin()
    # improve_first()
    # imporver_second()
    # user_improve()
    user_sqrt_imporve()