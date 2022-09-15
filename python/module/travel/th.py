class Thpackage:
    def detail(self):
        print("태국 패키지 3박 5일")
    def price(self):
        print("50만원")
        
if __name__=="__main__":
    print("Thpackage 직접실행")
    print("이문장은 모듈을 직접실행할때만 실행")
    trip_to=Thpackage()
    trip_to.detail()
else:
    print("Thpackage 외부 모듈 실행")        