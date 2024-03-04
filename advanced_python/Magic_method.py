import tempfile


class Magic_():
    def __init__(self,itemse,key,number_1,number_2):
        self.key=key
        self.itmes=itemse
        self.n1=number_1
        self.n2=number_2

    def __detaiL__(self):
        print("key= {} itmes= {}".format(self.key,self.itmes))
        
        return None
    def detail(self):
        print("detail")
    def __str__(self):
        print("__repr__ excute")
    def __add__(self):
        print("hello")
if __name__=="__main__":
    m=Magic_("dsne", 5,1,2)
    m.__detaiL__()
    m.detail()
    
    temp=print(m.__add__())
    print(dir(m))
    print(temp)

