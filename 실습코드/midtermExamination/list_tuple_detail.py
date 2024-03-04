n1=list('abc') #햇갈림 abc를 튜플로본다 [('abc')] 일시 한곳에
test=[('abc')]
n2=list([1,2,3])
n3=list((1,2,3))
n4='a','b','c' #튜플로 생성된다 햇갈림
n5=tuple('KZY') #햇갈림
data=[1,2,3]
data_2=("kello","jello","dsban")
print(test)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

x,y,z=data #리스트로싼것을 언패킹 중요함

print(x,y,z)
print(type(x)) #type int

m,n,t=data_2 #튜플을 언패킹하였더니 type str
print(m,n,t)
print(type(m)) #type str



test=[11,22,33,44,55,66,77]

print(test[-4:1:-1])