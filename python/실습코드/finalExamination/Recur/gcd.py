from typing import *
def gcd(x:int,y:int)->int:
    if y==0:
        print(x)
        return x 
    else:
        gcd(y,x%y)
        
if __name__=="__main__":
    print("두 정수값의 최대공약수를 구합니다")
    x,y=map(int,input().split())
    if x<y:
        x,y=y,x
    gcd(x,y)
    