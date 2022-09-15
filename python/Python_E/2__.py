#2주차 강의
#3장 조건문 
#논리값
#if문
#예외처리

#bool p.102

#논리값 bool자료형 참과 거짓을 나타내는 자료형 boolean
#True 또는 False두가지 값중 하나만 가질수있다
#0을제외한 모든숫자는 True 0=False
#문자열 공백을제외한 모든문자는 True
#None->False
#{}[] 빈리스트 ->False 값이 없는경우 False
#{1,2,3} True set 자료형

a=1
print(bool(a==1))


#논리연산자
#x or y x와y둘중 하나만참이면 ->참
#x and y x와y모두 참->참
#not x x가 거짓->참

#조건문
if a>2:
    print("a는 2이상")
elif a>1:
    print("a는 1이상")
else:
    print("a는1미만")

#조건문과 논리연산자
# age=input("나이를 입력")
# gender=input("성별입력")

# if (age>='20' and gender=="남성"):
#     print("20이상 남자")
# else:
#     print("아님")
    
#try except

# try:
#     num=3/0
#     print(num)
# except ValueError:
#     print("value error")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("error")

str="string"
try:
    print("hello")
    isint=int(str)
    print("world")
except:
    isint="변환불가"
print('Done',isint)