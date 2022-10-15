#Broadcasting
import numpy as np

a=np.array([[1,2,3],[4,5,6]])

b=a+3

print(b)
print()

data=np.arange(1,10,1,dtype=np.float32).reshape(3,3)
print(data)
print()

b=data+np.arange(3)
print(b)
print()

#indexing sliceing

a=np.arange(20).reshape(5,4)
print(a)
print()

print(a[0:2,3])
print()
print(a[2,3])
print()

