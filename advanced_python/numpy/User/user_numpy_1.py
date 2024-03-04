#numpy 요소간의 연산

import numpy as np
import random

a=np.arange(1,11,1).reshape(2,5)
b=np.arange(11,21).reshape(5,2)
c=np.random.randint(1,10,size=10)
print(c)


# c=a+b

# print(a)
# print()
# print(b)
# print()
# print(c)
# #요소들간의 단순 더하가

c=np.dot(a,b)# 행렬의 곱생성
print(c)
print()

#axis이해하기 
arr=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
data=np.array(arr)
print(data)
print()
s1=data.sum(axis=0)
print(s1)
print()

s2=data.sum(axis=1)
print(s2)
print()

s3=data.sum(axis=2)
print(s3)
print()

#append insert delete 속성 사용하기


a=np.random.randint(1,10,size=10).reshape(2,5)
print(a)
print()

a=np.insert(a,2,[1,2,3,4,5],axis=0) #axis=0밑방향을 기준으로 2번째에다가 데이터 삽입
print(a)
print()

a=np.insert(a,5,5,axis=1) #axis=1 옆방향을기준으로 6번째칸에 데이터삽입
print(a)
print()

a=np.append(a,[[0,0,0,0,0,0]],axis=0) #append는이중괄호필요 =>arr차원일치 필수!!!!!!!!
print(a)
print()


a=np.delete(a,3,axis=0)
print(a)
print()

a=np.delete(a,5,axis=1)
print(a)
print()
print(a.ravel()) #1차원으로 전부 풀기ㄴ