"""
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주input 사이즈 검사어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""

count=int(input())
data=input()
data=data[:count]
buffer=list(data)
total=0
for i in buffer:
    total+=int(i)
    
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