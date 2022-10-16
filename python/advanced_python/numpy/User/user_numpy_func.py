#filtering
#searching
#boolean indexing

import numpy as np


a=np.arange(20).reshape(4,5)
print(a)
print()

rows=np.array([True,False,False,True]) #0,3번째 행만 true이므로 값을 추출한다

b=a[rows,:] #boolean indexing

print(b)
print()

filter=a%2==0 # 행렬이 %2==0일떄 true할당 아닐떄 false할당
newarr=a[filter] #true인값만 모아서 새로운 arr을만든다

print(filter)
print()
print(newarr)
print()


arr=np.random.randint(1,6,size=15).reshape(5,3)
print(arr)
print()
data=np.where(arr==5)
print(data)

