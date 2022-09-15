class Dog:
    kind="강아지"
    def __init__(self,host):
        self.host=host


    def detail(self):
        print("나는 {0} 주인은{1}".format(self.kind,self.host))


class Super_dog(Dog):
    kind="슈퍼 강아지"
    def __init__(self,host):
        Dog.__init__(self,host)
    def detail(self):
        print(f"나는 {self.kind} 주인은{self.host}")




if __name__=="__main__":
    print("모듈 직접실행할때만 실행됩니다")
else:
    print("모둘 외부실행")
    
    
       

        
                              