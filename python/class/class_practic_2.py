class Fourcal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
        
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result            
    def mul(self):
        result=self.first*self.second
        return result

class More_Fourcal(Fourcal):
    def pow(self):
        result=self.first**self.second
        return result


class safe_Fourcal(Fourcal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.frist/self.second




number2=safe_Fourcal(3,0)

print(number2.div())






