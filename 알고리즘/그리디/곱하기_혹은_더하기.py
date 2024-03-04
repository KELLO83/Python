'''
각 자리가 0부터0로만 이루어진 문자열s가주어질떄
왼쪽부터 오른쪽으로 하나씩 모든숫자를 확인하며 숫자사이에 'x'혹은 '+'
연산자를 넣어 결과적으로 만들어질수있는 가장큰수를 구하는
프로그램을 작성하시오
'''
import collections

N = list(input("input data"))
N = collections.deque(map(int,N))
sum = 0
first_data = N.popleft()
secode_data = N.popleft()
print(first_data)
print(secode_data)

if first_data == 0  or secode_data == 0:
    sum = first_data + secode_data
else:
    sum = first_data * secode_data
    
for i in N:
    if i == 0 or i == 1 :
        sum +=i
    else:
        sum *=i
        
print(sum)
        
