n1=list('abc') #햇갈림
n2=list([1,2,3])
n3=list((1,2,3))
n4='a','b','c' #튜플로 생성된다 햇갈림
n5=tuple('KZY') #햇갈림
data=[1,2,3]
data_2=("kello","jello","dsban")
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

x,y,z=data #리스트로싼것을 언패킹 중요함

print(x,y,z)
print(type(x)) #type int

m,n,t=data_2 #튜플을 언패킹하였더니 str type을 가지게도었다
print(m,n,t)
print(type(m)) #type str