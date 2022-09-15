import sys
data=list(map(int,input().split()))

temp=sys.stdin.readline().rstrip()#sys 모듈을 이용한 input보다 빠르게 받기 rstrip엔터키제외
print(data,end="") #end속성을 이용하여 줄바꿈을 하지않는다
print("끝")

result=(lambda a,b:a+b)(3,7) #람다표현식 함수를 한줄로 간단하게 정의한다 
print(result)


array=[('kello',30),('dsban',20),('tsm',100)]

print(sorted(array,key=lambda x:x[1]))

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

result=map(lambda a,b:a+b,list1,list2)

print(list(result))
print(result)



