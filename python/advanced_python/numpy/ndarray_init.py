import numpy as np
import random
#여러가지 nd array의 생성방법

a=np.linspace(0,11,11) #start 지점부터 end지점까지 step을 컴파일이 알아서 정하면서 일정Step공간을가진 N개의 원소를 만든다
#닫힌구간 [0,11]사이에서 N개 요소를만든다 start end를 포함
print(a)
print()

b=np.zeros((3,4)) #shape모양의 행렬을만들면서 0으로 전부초기화
print(b)
print()

c=np.ones((1,2)) #shape모양의 행렬을 만들면서 1로 초기화
print(c)
print()

d=np.empty((2,2)) #원소가 초기화되지않은 배열생성
print(d)
print()

e=np.full((2,2),random.randint(1,100)) #shpae모양의 사용자가 입력한value값으로 전부초기화
print(e)
print()
print("---------------------")

f=np.random.randint(10,size=(2,2)) #[start,end) 열린구간부터 닫힌구간까지  size갯수만큼 원소를 만든다
#size는 N차원도 가능 (2,2) 2행2열인 원소를 0,9사이의 숫자에서 만든다
print(f)
print()

g=np.random.rand(2,3) #균등분포를 갖는 난수를 발생시킨다
print(g)
print()

h=np.random.randn(3,2) #가우시안 정규분포를갖는 난수를 발생시킨다
print(h)
print()

# rand randn 차이점 꼭 인지하기

