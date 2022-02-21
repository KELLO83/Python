import pprint

from numpy import number

a=5
b=3

t1=a+b

t2=a/b

t3=a%b 

t4=a**b

t5='hello world'

t6='kello\n\abye'

pprint.pprint(locals())

print(t6)

t7="a=%d ,b=%f"%(3,5.44)

print(t7)

print("%10s"%"hello") #오른쪽으로 10칸댕긴후 오른쪽부터 채운다

print("%-10s"%"hello") #왼쪽으로 10칸할당후 왼쪽부터 채운다

print("%0.4f"%3.12345) #소숫점 4자리까지 표시하기 

print("%10.4f"%3.1234567) #10칸할당후 10칸의 왼쪽부터 소숫점 4자리까지 출력한다

number=3
grade='A+'

print(f"hello {number} grade={grade}")

print("{0:>10}".format("hi"))

print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))

print("{0:0.4f}".format(3.123456))

#문자열 내장함수

a="  KEllo  "

print(a.count('o'))

print(a.find('l'))

print(a.index('o'))

print('----'.join('abcd')) #a찍고 -----찍고 b찍고 ----찍고

print(a.upper())

print(a.lower())


print(a.lstrip()) #왼쪽 공백 지우기

print(a.rstrip()) #오른쪽 공백 지우기

print(a.strip()) #공백 전부 지우기

print(a.replace('lo'," hello world")) # a의 문자열 lo를 hello world로 바꾼다

b='Life is good'

value=b.split('is') #is 를 기준으로 나눈다 이후 list 로반환한다

print(value)

print(type(value))


a=list()


