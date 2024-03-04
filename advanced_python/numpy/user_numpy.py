import numpy as np
import random 
arr=np.arange(1,20,2).reshape(2,5)
#2행 5열을 만듭니다

print(arr)
print(arr.ndim) #2행 ndim=axes의수 
print(len(arr.shape)) # arr.ndim
print(arr.shape) #2행 5열을 tuple형태로 전달받습니다
print(arr.size) # 배열요소의 갯수
print(arr.dtype)
print(arr.itemsize)

print("------------------")


data=np.random.randint(1,100,size=20).reshape(2,2,5)
#2차원 2행 5열
print(data)
print(len(data.shape)) #3차원 리스트 
print(data.ndim)
print(data.shape)


print("-----------------------")


list_=[[1,2,3,4],[5,6,7,8]]
data=np.array(list_)
print(data)
print(len(data.shape))
print(data.ndim)

print("------------------------")


data=np.linspace(0,100,10).reshape(5,2)
print(data)
print()
data=np.empty((2,3)); #empty shape의 튜플형태로 전달해야한다
print(data)
print()


data=np.ones((2,3))
print(data)
print()

data=np.zeros((3,3))
print(data)
print()

data=np.full((3,3),random.randint(0,10))
print(data)
print()

data=np.random.rand(3,2) #3행 2열의 실수를 [0,1)구간에서 생성 
print(data)
print()

data=np.random.randn(3,3) #가우시안 정규분포 평균0 분산이 1인 3행3열 데이터생성
print(data)
print()
