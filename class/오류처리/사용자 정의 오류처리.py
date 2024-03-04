class over_number(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try: 
    print("한자리 숫자 나누기 전용 계산기 입니다")
    n1=int(input("첫번쨰 숫자입력"))
    n2=int(input("두번쨰 숫자 입력"))
    if n1>=10 or n2>=10:
        raise over_number("{0} {1}".format(n1,n2))
    print("{0}/{1} ={2}".format(n1,n2,(n1/n2)))

except ValueError:
    print("범위초과")


except over_number as err:
    print(err)
finally:
    print("오류검사 완료")
    
    
       
    
    

     
    
    
        