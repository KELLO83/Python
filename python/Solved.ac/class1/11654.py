#아스키코드
# 알파벳 소문자 대문자 숫자0~9중 하나가 주어졌을때 주어진글자의 아스키코드값을 출력하라
# 문제해결중요요소 ord():문자를 아스키코드로 변횐해준다 chr(숫자):숫자에맞는 아스키코드를 반환한다
data=input() #입력받는것이 숫자인지 문자인지 구별이필요하다 문제핵심!!!!
try:
    res=ord(data)
except:
    res=chr(data)  # type: ignore
    
print(res)