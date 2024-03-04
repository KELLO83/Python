#ndarry의 연산방법

import numpy as np
import random

a=np.random.randint(10,size=(2,2))
b=np.random.randint(10,size=(2,2))

print(a)
print()
print(b)
print()

c=a+b #요소들간의 합
print(c)
print()

d=a*b #요소들간의 곱
print(d)
print()


print(np.dot(a,b)) #행렬의 곱 
print()

print("--------------------")

data=np.array([1,2,3]) 
a=np.append(data,4)
print(a)
print()

data=np.array([[1,2,3],[4,5,6]])
a=np.append(data,[[7,8,9]],axis=0) #원본이 2차원이면 2차원으로 인수를 줘야한다
#0축에다가 추가 0행추가 
print(a)
print()


a=np.insert(data,1,-1,axis=0)
print(a)
print()

# Broadcasting

data=np.arange(3)+5
print(data)
print()

data=np.ones((3,3))+np.arange(3)
print(data)
print()


data=np.arange(3).reshape(3,1)+np.arange(3)
print(data)
print()

#결론 행과열이 맞지않는 행렬을 서로의 행과열이 최소지점에서 만나는 곳에서 연산을시작한다
