def add(x,y): 
    assert isinstance(x,int),'Expected int'
    assert isinstance(y,int) ,'Expected int'
    return x+y


print(add(3,2))
print(add(3,1.5))
