class Over(Exception):
    def __init__(self,msg):
        self.msg=msg
        
    def str(self):
        print(f"{msg}")    
        
try:
    n1=int(input("첫번쨰 숫자입력"))
    n2=int(input("두번쨰 숫자입력"))
    
    if n1>10 or n2>10:
        raise Over("범위초과")
except Over as e:
    print(e)
    
    
    
    
    
    
    
    
    
    
    
    