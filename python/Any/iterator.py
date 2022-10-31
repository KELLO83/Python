# it test
#iterator객체 -> list string dict tuple for문 enumerate 순회가능한 객체라 

t1=set([1,2,3,1])
print(t1)
print(type(t1)) #순서는이쓴데 set안에서 인덱싱을 magic method 지원x
for i in t1: #->list stirng set 요소를 하나씩꺼내가면 들어가는거죠 {1,2,3} -> 1 2
    print(i) 

print("--------------------------")

t2={'one':"1st","two":"2sd","third":"3rd"}
print(t2)
print(type(t2))

for i in t2:
    print(i)

print("-----------------------------")


t3="iterable"
print(t3)
for i in t3:
    print(i)


print("-------------------")

t4=(5,4,3,2,1)
print(t4)

for i in t4:
    print(i)    


print('-----------')

for i in enumerate(t1):
    print(i)


    
    
    