import numpy as np
import numpy.linalg as npl


a=np.eye(3) #n*n 단위행렬 생성 
print('a\n',a)

b=np.array([[1,3],[2,4]])
print('b\n',b)
print('역행렬\n',npl.inv(b)) #b의 역행렬 B*B^-1=I B행렬 * B역행렬=단위행렬


a=np.arange(12).reshape(3,4)
b=np.arange(24).reshape(2,4,3)
print(a)
print(a.T) #A행렬의 전치행렬 구하기
