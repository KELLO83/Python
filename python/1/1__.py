import imp
import pprint


def fn(a:int)->True: # a:int a는 int형 fn이라는 함수는 True를 리턴한다고 사용자가 편의상 적는것
    print("hello{}".format(a))
    a:str='1'
    b:int=2
    print(f"{a},{b}")
    
add=lambda a,b:a+b
a=3
b=5

fn(3)

print(f"{a},{b}",sep='---',end="\n") #sep 는 각 변수찍고 그다음 변수찍을때 사이에 넣는 문자또는 숫자 end 는 모든 문자열을찍고난후 찍을 문자또는 숫자

pprint.pprint(locals()) #로컬 지역변수 디버그창처럼 터미널에 보여준다 변수에 어떤값이 들어있는지 


def numMatchingSubseq(S:str,words:list[str])->int:
    a=0
    
    for b in words:
        c=0
        for i in range(len(b)):
            d=S[c:].find[b[i]]
            if d<0:
                a-=1
                break
            else:
                c+=d+1
        a+=1    
    return a    

if a is None: #is id값을 비교하는 함수
    pass

a=[1,2,3,4]

if 5 in a:  # elem in a  리스트 a에 elem이라는 요소가있는지 검사
    print("3이있어요")
else:
    print("1,2,3,4이외의 숫자")
    
    
