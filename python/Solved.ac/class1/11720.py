"""
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주input 사이즈 검사어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""

count=int(input()) #몇번 숫자를 입력할것인가
data=input() #dat str형태
data=data[:count] # data  [:3] # [1,2,3,4,5] -> [:3] -> [1,2] 
buffer=list(data) #list ->
total=0 
for i in buffer: #리스트안에 요소를 하나씩꺼내면서 반복문을도는건데
    total+=int(i) # str int sum
# buffer['1','3','5']
# total=total+int('1')->total+1 
# total=total+ing('3)->to
# 면접자 발표자이 코드도 풀어보고 서로 자기발표문제 팀원의 문제도 푸는거죠
# 언어 문제가  팀원끼리 협의를 python c++
# 핵심을 면접자 내조원이 내문제를 안풀어봤는데 어떻게 피드백을 주느냐?
# 내가면접자역하리억자ㅣ 팀원의 문제를 풀고 팀원 생각치 
# 결론 -> 발표자가 면접자코드를 짜본게  발표자코드에대해서 내가짠거랑 밸표자 
# 
print(total)


""" ->에러발생 이유는?
sum=0
while True:
    count=int(input())
    if count<1 or count>100:
        continue
    data=int(input())
    n_list=list(map(int,str(data)))
    if len(n_list)!=count:
        continue
    else:
        for i in n_list:
            sum+=i
        break
            
print(sum)
"""