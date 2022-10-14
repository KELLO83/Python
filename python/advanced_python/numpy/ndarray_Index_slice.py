#ndarry indexing slicing 사용법

import numpy as np


data=np.arange(10) # 1,2,3,4,5,6,7,8,9
print(data[:])
print(data[::2])
print(data[:-3:-1])
print(data[7:2:-2])


data=np.arange(20).reshape(5,4)
print(data)
print()
print(f"{data[2,3]}\n\n{data[0:5,1]}")