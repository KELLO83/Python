"""
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.
"""

count=int(input()) #
buffer=list() # [] , 

for i in range(count):
    roop,string=map(str,input().split()) # 3 5 str 3 5 map객체로  roop=3 string="문자열s"   
    roop=int(roop) #'3' int 3 roop=3 string=ABC
    for j in range(len(string)):        
        print(roop*string[j],end="") 
    print()
    # for j in range(len(string)): #차음시도 range(roop) ->len(string) 수정 rarnge(roop) ABC ROOP=LEN(STR)  ABCD ROOP=!LEN(STR)
    #     for k in range(roop):
    #         buffer.append(string[j]) #ABC 3번반복 AAA BBB CCC
    #바깥루프는 문자열의 길이만큼 
    #안쪽루프는 MAP으로받은 ROOP만 반복문을
    # print(''.join(buffer)) #STRING LIST STRING STR.JOIN(list) ->str AAA BBB CCC
    # buffer.clear() #list초기화
    



