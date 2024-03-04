#정규식 표현
import  re


p=re.compile("ca.e")
# . (ca.e)은 하나의 문자를 의미한다 ->care,cafe,case 
# ^ (^de) 문자열의 시작  -> desk
# $ (se$) 문자열의 끝 -> okse

def print_match(m):

    if m:
        print("m.group()",m.group()) #일차하는 문자열 반환
        print("m.string",m.string)  #입력받은 문자열
        print("m.start():",m.start()) #일치하는 문자열의 시작 index
        print("m.end()",m.end()) #일치하는 문자열의 끝
        print("m.span()",m.span()) #일치하는 문자열의 시작//끝 index
    else:
        print("매칭되지않음")
    
    
# result=p.match("caffe")
# print_match(result)


# result1=p.search("good cafe")
# print_match(result1)


result2=p.findall("good cafe") #리스트 형태로 반환
print(result2)


# k=p.match("careless") #match:주어진 문자열의 처음부터 일치하는지 확인하는것 
# print_match(k)


# str=p.search("good care") # serarch:주어진 문자열중에 일치하는것이 있는지 확인하는것
# print_match(str)

# list=p.findall("good care cafe") # findall:일치하는 모든것을 리스트 형태로 반환
# print(list)



#정리 

# 1. p=re.compile("원하는 정규식 형태")
# 2. m=p.match("비교할 문자열") :주어진문자열이 처음부터 일치하는지 확인
# 3. m=p.search("비교할 문자열") :주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst=p.findall("비교할 문자열") :일치하는 모든것을 리스트 형태로 반환

# 원하는 형태 정규식
# . (ca.e)은 하나의 문자를 의미한다 ->care,cafe,case 
# ^ (^de) 문자열의 시작 
# $ (se$) 문자열의 끝




