#Labda lambda 인수:식
from functools import reduce
g=lambda x,y:(x*y)
print(g(2,3))
h=((lambda x,y:x+y)(2,3))
print(h)

arr=[1,2,3,4]
arr2=[10,11,12,13]

fun=lambda x,y:(x*2,y*2)

data=list(map(fun,arr,arr2)) #튜플형태로 전달 arr arr2를 fun lamda로 전달한다
print(data)

arr=[1,2,3,4,5,6,7,8,9]

fun=lambda x:x%2==0

data=list(map(fun,arr))
print(data)

data=list(filter(fun,arr)) #Sequence의 각요소를  함수에 적용후 반환값이 true인것만 묶어서 반환한다
print(data)


func=lambda x:True if x%2==0 else False
print(list(filter(func,arr)))

#reduce

func=lambda x,y:x+y
print(reduce(func,arr)) #각요소들은 계속 더해간다
