import time
from typing import Any
def deco(func):
    def wrapper():
        print(func.__name__,'함수시작')
        func()
        print(func.__name__,'함수종료')
    return wrapper
@deco
def get_time():
    print('현재시간 {}',time.time())


get_time()

def out(num):
    def inner():
        print(num)
    return inner

f1=out(3)
f1()


class deco:
    def __init__(self,func) -> None:
        self.func=func
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(self.func.__name__)

@deco
def kkk():
    print("hello")
    
kkk()

def add(x,y):
    assert isinstance(x,int),'Expected x'
    assert isinstance(y,int),'Expected y'
    return x+y


print(add(2.1,3))

