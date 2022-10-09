arr=[[i+j for i in range(4)] for j in range(3)] #2차원 list comprehension
#변수활용 열의갯수만큼 반복 이후 행의갯수만큼 반복
print(arr)
string=[c*3 for c in "HELLO"]
print(string)

#리스트컴프리핸션 필터링 사용하기

arr=[i for i in range(10) if i%2==0]
print(arr)


# list comprehesnion 참과 거짓인경우 분할
arr=[i if i%2==0 else False for i in range(10)] #참인경우 짝수 아닌경우 false출력
print(arr)

# 반복의 중첩
#열 4 행 3 인데 1차원리스트이므로 1차원공간 => 열만 고려한다
arr=[c for c in range(4) for r in range(3)]
print(arr)
"""
arr=[]
for c in range(4):
    for r in range(3):
        arr.append(c)
"""
# 2차원 list comprehension
arr=[[c for c in range(4)] for r in range(3)]
print(arr)

# 반복의 중첩에서 원소를 리스토 담은것
arr=[[c] for c in range(4) for r in range(3)]
print(arr)

#2차원 리스트 편평화

arr=[[1,2,3],[4,5,6],[7,8,9]]

flat_arr=[i for row in arr for i in row]
print(flat_arr)

#집합 딕셔너리는 순서를 유지할수없다 순서가 계속 달라질수도있음
arr=[1,1,2,3,3,4]
arr_set={i * i for i in arr}
print(arr_set)


#딕셔너리 컴프리핸션

dict1={1:"first",2:"second",3:"third"}

dict2={val:key for key,val in dict1.items()}

print(dict2)


