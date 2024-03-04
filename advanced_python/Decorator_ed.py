import time
from typing import Any
def outer(num):
    def inner():
        print(num)
    return inner

f1=outer(3)
f1()


def time_decorator(func):
    def decoratrd(*args,**kewars):
        #전처리코드
        start=time.time()
        print(start)
        func(*args,**kewars)
        #후처리 코드
        end=time.time()
        print(end)
    return decoratrd

@time_decorator
def myfunc():
    print("hello")
    
myfunc()


class TimeDecorator:
    def __init__(self,func) -> None:
        self.func=func
        
    def __call__(self, *args: Any, **kwards: Any) -> Any:
        start=time.time
        self.func(*args,**kwards)
        end=time.time()
        print(f"Elsape time  {end-start} seconds")
        
        