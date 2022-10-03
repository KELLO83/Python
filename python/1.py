class Point():
    def __init__(self,x,y) -> None:
        self.__x=x
        self.__y=y
    def __str__(self):
        return f"({self.__x},{self.__y})"
    def __eq__(self, object: object) -> bool:
        if self.__x==object.__x and self.__y==object.__y:
            return True
        return False
p=Point(1,2)
print(p)
k=Point(1,3)
t=Point(1,2)

print(p==k)
print(p==t)