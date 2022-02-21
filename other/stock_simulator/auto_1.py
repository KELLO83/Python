import queue

basic_count = 10
basic_total = 100000
basic_stock_price = 3000

#test
#2번째 수정.


def entry():

    result = list()
    while(True):
        value = input("상승/하락 %입력")
        result.append(str((value)))
        print("{0}%입력".format(value))

        exit = input("종료원할시 1입력")
        if exit == '1':
            print("입력을 종료합니다")
            break
    return result    
class Synthesis():
    def __init__(self,value, basic_count, basic_total, basic_stock_price):
        self.count = basic_count #보유중인 주식 수량
        self.stock_price = basic_stock_price #현재 주식 가격
        self.wallet = basic_total #내가 현재지갑 돈
        self.count_sell=0  #현재 내가 지금까지 총 팔은 주식수량
        self.count_buy=0   #현재 내가 지금까지 총 매수한 주식수량
        self.result=list()
        self.value=value
        
    def stock(self):
       
        while(True):
            if not value: #if len(value)==0
                print("list is empty")
                break
            else:
                temp = value.pop(0)

            temp_1 = temp[0]
            temp_2 = temp[1]
            temp_3 = temp_1+temp_2
            if temp_3 == "상승":

                Rate_Change = temp[2:]
                print("상승")
                print("2주를 매도합니다")
                self.stock_price = self.stock_price + \
                round(float(((int(self.stock_price)*int(Rate_Change))/100)), 2)

                if self.count != 0:
                    print("2주매도완료")
                    self.count = self.count-2
                    self.wallet = round(self.wallet+(self.stock_price*2),2)
                    self.count_sell=self.count_sell+2
                    print("지갑에 남은돈{0} 현재 보유 주식수{1}".format(self.wallet, self.count))
                else:
                    print("보유수량이 없습니다 ")
                    print("매도실패")

            if temp_3 == "하락":
                Rate_Change = temp[2:]
                print("하락")
                print("2주를 매수합니다")
                self.stock_price = self.stock_price - \
                round(float(((float(self.stock_price)*int(Rate_Change))/100)), 2)

                if (self.stock_price*2) > self.wallet:
                    print("지갑잔고부족")
                    print("2주매수 실패")
                else:
                    print("2주매수를 진행합니다")
                    self.wallet = round(float(self.allet-(self.stock_price*2)), 2)
                    self.count = self.count+2
                    self.count_buy=self.count_buy+2
                    print("지갑에 남은돈{0} 현재 보유 주식수{1}".format(self.wallet, self.count))
    
        
        self.result.append(self.count)
        self.result.append(self.wallet)
        self.result.append(self.count_sell)        
        self.result.append(self.count_buy)
        self.result.append(self.stock_price)
                                
    def inspect(self,basic_count,basic_total,basic_stock_price):
        
        print("원금 시작한 자산{:.2f}".format(basic_total))
        print("현재 가지고있는 수량{}".format(self.result[0]))
        print("현재 지금까지 전부 매수수량{} ".format(self.result[3]))
        print("현재 지금까지 전부 매도수량{}".format(self.result[2]))
        print("현재 보유자산{}".format(self.result[1]))
        print("총 평가자산{}".format(self.result[1]+self.result[4]*self.result[0]))
        profit=round(float(self.result[1])-float(basic_total),2)
            
        if profit>0:
            print("수익금은{}입니다".format(profit))
            percent=round(((self.result[1]-basic_total)/(basic_total))*100,2)
            print("수익률은{}%입니다".format(percent))
        else:
            print("손익금은{}입니다".format(profit))
            percent=round(((self.result[1]-basic_total)/(basic_total))*100,2)
            print("손실률은{}%입니다".format(percent))
            


                    

    
    
value = list()
value = entry()
print("value", value)

a1=Synthesis(value,basic_count,basic_total,basic_stock_price)

a1.stock()
a1.inspect(basic_count, basic_total, basic_stock_price)

if __name__=="__main__":
    print("내부 모듈 실행")