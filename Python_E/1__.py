#세자리의 수를 입력받아 백의자리 십의자리 일의자리 떼어내기

number=int(input("세자리의 숫자를 입력하세여"))
print("세자리의 숫자 {}".format(number))

n1=number//100
print("백의 자리={}".format(n1))
n2=(number-n1*100)//10
print("십의 자리 ={}".format(n2))
n3=(number-n1*100-n2*10)
print("일의 자리 ={}".format(n3))

#슬래시 한개/ -> 소숫점을 남김
#슬래시 두개 //-> 몫만 준다 c언어의 /효과이다 
#슬래시 한개 두개 착오금지!!

