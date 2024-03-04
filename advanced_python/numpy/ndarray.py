import numpy as np

#axes 차원의 번호
#rank 차원의 수
#shape ndarray의 모양

data=np.arange(1,30,2).reshape(3,5) #arange=range 행의갯수 3 열의갯수 5 3행 5열로 변환
"""
Sequence types =>값이 연속적으로 이어진 자료형
python의 range는 오직 정수들의 Sequence만 만들수있다
NP의 arange 실수들도 가능
"""
print(data)
#Rank가 2인 배열 shape는 (3,5)입니다

print(data.ndim) #axes의수 수:rank

print(len(data.shape)) # data.ndim==len(data.shape)

print(data.shape) #튜플의 형태로 전달한다

print(data.size) # 배열 요소의 총 갯수

print(data.dtype) #배열요소의 자료형

print(data.itemsize) #각 요소의 크기 int형 =>4

print()
#---------------------------------------------------------------
Numpy=np.arange(1,30,2,dtype=np.float32)

print(Numpy)

print(Numpy.ndim)

print(len(Numpy.shape))

print(Numpy.shape)

print(Numpy.size)

print(Numpy.dtype)

print(Numpy.itemsize)