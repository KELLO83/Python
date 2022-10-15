data=[[i+j for i in range(4)]for j in range(3)] #바깥이행 안쪽 열 3행 4열 생성
print(data)

data=[i for i in range(20) if i%2==0] #i%2==0인경우만 담는다
print(data)

data=[i if i%2==0 else -1 for i in range(20)] #if else 두가지 경우
print(data)

#반복의 중첩

arr=[i for i in range(4) for r in range(3)] #1차원 배열 생성
print(arr)

arr=[[i]for i in range(4) for r in range(3)] #2차원 배열 생성
print(arr)

#Dictionary Comprehension

dict1={1:'frist',2:'second',3:"third"}

dict2={key:val for key,val in dict1.items()}
print(dict2)