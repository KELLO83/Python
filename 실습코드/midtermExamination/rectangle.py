#직사가형 넓이로 변의 길이구하기



area=int(input("직사각형의 넓이를 입력하세요"))

for i in range(1,area+1): #1부터 시작해야한다 0은 어떤수를 곱하더라고 0
    if i*i>area: #정사각형 서로곱한것이 area보다클경우
        break
    if area%i!=0: #정수로 안 나누어떨어진다면
        continue
    print("{} x {}".format(i,area//i))



"""
만약 넓이가 20인 직사각형
4*4=16

1*16
2*8
3*5.3
4*4
5.3*3 중복인 구간이 존재한다
"""