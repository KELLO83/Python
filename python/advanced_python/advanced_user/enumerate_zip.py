#enumerate Sequence 데이터를 입력받아 index를 포함하는 enumerate객체를 반환하는 함수

data=enumerate("hello world")
print(data)
for i in range(len("hello world")):
    print(next(data))
    


data='test'
data2='psma'
#zip 여러개의 Sequence를 인자로 받고 각객체가 담고있는 원소를
#튜플형태로 차례로접근할수있는 Sequence를 반환 Sequnece=>모두값이 연속적으로 이루어져있다
buffer=zip(data,data2)
print(buffer) #zip객체를 받고있으므로 메모리주소가 나온다

# for i in buffer:  
#     print(i)


pairs=zip([1,2,3],['A','B','C'])

c,d=zip(*buffer)
print(c)
print(d)