import queue

basic_count = 10
basic_total = 100000
basic_stock_price = 3000


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

def stock(value, basic_count, basic_total, basic_stock_price):
    count = basic_count #보유중인 주식 수량
    stock_price = basic_stock_price #현재 주식 가격
    wallet = basic_total #내가 현재지갑 돈
    count_sell=0  #현재 내가 지금까지 총 팔은 주식수량
    count_buy=0   #현재 내가 지금까지 총 매수한 주식수량
    
    while(True):
        if len(value) == 0:
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
            stock_price = stock_price + \
            round(float(((int(stock_price)*int(Rate_Change))/100)), 2)

            if count != 0:
                print("2주매도완료")
                count = count-2
                wallet = round(wallet+(stock_price*2),2)
                count_sell=count_sell+2
                print("지갑에 남은돈{0} 현재 보유 주식수{1}".format(wallet, count))
            else:
                print("보유수량이 없습니다 ")
                print("매도실패")

        if temp_3 == "하락":
            Rate_Change = temp[2:]
            print("하락")
            print("2주를 매수합니다")
            stock_price = stock_price - \
            round(float(((float(stock_price)*int(Rate_Change))/100)), 2)

            if (stock_price*2) > wallet:
                print("지갑잔고부족")
                print("2주매수 실패")
            else:
                print("2주매수를 진행합니다")
                wallet = round(float(wallet-(stock_price*2)), 2)
                count = count+2
                count_buy=count_buy+2
                print("지갑에 남은돈{0} 현재 보유 주식수{1}".format(wallet, count))
    result=list()
    
    result.append(count)
    result.append(wallet)
    result.append(count_sell)        
    result.append(count_buy)
    result.append(stock_price)
    
    return result   
                    
def inspect(result,basic_total):
    
    print("원금 시작한 자산%.2f" %basic_total)
    print("현재 가지고있는 수량{}".format(result[0]))
    print("현재 지금까지 전부 매수수량{} ".format(result[3]))
    print("현재 지금까지 전부 매도수량{}".format(result[2]))
    print("현재 보유자산{}".format(result[1]))
    print("총 평가자산{}".format(result[1]+result[4]*result[0]))
    profit=round(float(result[1])-float(basic_total),2)
        
    if profit>0:
        print("수익금은{}입니다".format(profit))
        percent=round(((result[1]-basic_total)/(basic_total))*100,2)
        print("수익률은{}%입니다".format(percent))
    else:
        print("손익금은{}입니다".format(profit))
        percent=round(((result[1]-basic_total)/(basic_total))*100,2)
        print("손실률은{}%입니다".format(percent))
        


                    

    
    
value = list()
value = entry()
print("value", value)

result=list()
result=stock(value,basic_count, basic_total, basic_stock_price)
inspect(result,basic_total)