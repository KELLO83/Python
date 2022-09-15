#미리정의가 되어있는 연산자를 다시 내가원하는 기능으로 변경하거나 수정한다 ...

class Gstring:
    def __init__(self,init,string,n1,n2):
        self.contents=init
        self.str_=string
        self.n1=n1
        self.n2=n2
    def __sub__(self,str_):
        count=0

        self.contents=self.contents.replace(self.contents,str_)
        count+=1
        return Gstring(self.contents,self.str_,self.n1,self.n2)
    
    def remove(self,str):
        return self.__sub__(str)
    
    # def __repr__(self):
    #     return str(self.contents)
    #     return None
    
    def test(self):
        print("{}".format(self.n2))
        
    def __add__(self):
        
        s1=self.a+self.b
        print(s1)
        return s1
if __name__=="__main__":
    string=Gstring("test","string",1,2)
    rs=string.__sub__("replace")
    print(rs)
    print(string.__repr__())
    print(string.__hash__())
    print(string.__class__)
    string.test()
