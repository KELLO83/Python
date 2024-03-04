class House:
    count=0
    def __init__(self,lcoation,house_type,deal_type,price,completion_year):
        self.location=lcoation
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
        House.count=House.count+1
        
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type\
            ,self.price,self.completion_year))
    def cnt(self):
        print("count={0}".format(House.count))
        
        
        
        
house_1=House("강남", "아파트", "매매", "10억","2010년")
house_2=House("마포","오피스텔","전세","5억","2007년")
house_3=House("송파", "빌라","월세", "500/50", "2000년")


house_1.show_detail()


house_1.cnt()
print(House.count)



