import calc_utils as tool

prices = []

#주식 종가 시세파일 읽기
filename = "C:\\vs code\\python\\stock_simulator\\두산퓨어셀_20191018.txt"
tool.readData(filename, prices)

#기초매입 수량
base_quantity = 15
#매수 수량
change_quantity = 15

#종가 / 등락폭 / 매수,매도 / 수량 / 잔고수량 / 총평가금액 / 원금 / 수익율 / 매도수익금

def main():    
    previous_price = prices[0]
    index = 1
    list_buy = []    #매수가격 기록용 리스트
    sum_quantity = 0 #잔고수량
    evaluation_price = 0 #총평가금액
    principal_price = 0  #원금
    cash = 0 #현금자산(예수금)
    asset = 0 #자산총액
    buy_sum = 0 #매입합계금액
    min_buy_ratio = -5  #수익율 -5% 단위로 매수.
    first_price = 0 # 거래시작 최초 금액
    last_price = 0 # 거래종료 마지막 금액

    print("=================================================================================================================================")    
    print("가격  전일등락폭  구분 수량 잔고수량  평균단가 =>(%)  | 총평가금액     예수금|    평가자산       원금   수익금   수익율")
    print("=================================================================================================================================")

    for price in prices:    
        change_ratio = tool.getFluctuationRatio(previous_price, price) #전일대비 등락율
        str_price = "{:,}".format(price)
        str_change_ratio = "{:-3.2f}".format(change_ratio)
        
        action = ""
        comment = ""
        
        previous_price = price
        last_price = price
        if index == 1:
            first_price = price
            quantity = base_quantity
            sum_quantity = base_quantity
            principal_price = quantity * price
            buy_sum = quantity * price
        else:
            quantity = change_quantity
            
        # 매도 기준 ? 이전 구매가 보다 올라간 경우만..... && 잔고수량이 0 보다 큰경우.   
        # todo ... 매도시 현재가 대비 0.8% 이상의 매수가격은 모두 매도 하는 로직 필요.....
        if change_ratio > 0 and tool.canSell(price, list_buy, 1) != -1 and sum_quantity > 0:        
            boughtPrice = tool.removeSell(price, list_buy, 1)
            action = "매도"        
            action = tool.setBlue(action)
            
            
            comment = ' ::> 매도금액:{매도금액} 이전구매가격:{이전구매가격} 수익금:{수익금} 수익율 {수익율}'\
                .format(매도금액="{:,}".format(price), \
                    이전구매가격="{:,}".format(boughtPrice) ,\
                        수익금="{:,}".format(price - boughtPrice) ,\
                            수익율="{:3.2f}".format(tool.getFluctuationRatio(boughtPrice, price))) 
                
            comment = tool.setBlue(comment)
            
            sum_quantity = sum_quantity - quantity #잔고수량
            buy_sum = buy_sum - ( quantity * price)        
            cash = cash + ( quantity * price ) # 현금자산        
        # 매수 기준 ? 수익율 -5% 단위 구간
        elif change_ratio < 0:        
            evaluation_price = sum_quantity * price # 총평가금액
            ratio = tool.getFluctuationRatio(buy_sum, evaluation_price) #수익율
            if ratio < min_buy_ratio:
                action = "매수"
                action = tool.setRed(action)
                principal_price = principal_price + ( quantity * price ) #원금
                sum_quantity = sum_quantity + quantity #잔고수량
                buy_sum = buy_sum + ( quantity * price)
                comment = ' ::> 매수전: 총평가금액 {총평가금액} 수익율 {수익율}'.format(총평가금액="{:,}".format(evaluation_price), 수익율="{:3.2f}".format(ratio)) 
                list_buy.append(price)
                list_buy.sort()
                
            else:
                quantity = 0
                action = "관망"
                action = tool.setYellow(action)
                
        else:
            # #매도/매수 없이 관망.....
            quantity = 0
            action = "관망"
            action = tool.setYellow(action)
        
        evaluation_price = sum_quantity * price # 총평가금액
        asset = evaluation_price + cash # 자산금액 = 총평가금액 + 예수금
        average_price = int( buy_sum / sum_quantity )# 평균단가
        average_price_ratio = tool.getFluctuationRatio(average_price, price)
        
        income  = (asset - principal_price)  # 수익금 = 자산금액 - 원금
        ratio = tool.getFluctuationRatio(principal_price, asset) #수익율
        
        str_evaluation_price = "{:,}".format(evaluation_price)
        str_cash = "{:,}".format(cash)
        str_asset = "{:,}".format(asset)
        str_principal_price = "{:,}".format(principal_price)
        str_ratio = "{:-3.2f}".format(ratio)
        str_income ="{:,}".format(income)
        str_average_price = "{:,}".format(average_price)
        str_average_price_ratio = "{:-3.2f}".format(average_price_ratio)
        
        
        #평균단가   
        # print("가격:%-6s  전일등락폭:%6s %%  구분:%-2s 수량:%-3d 잔고수량:%-3d | 평균단가:%-6s 총평가금액:%-7s  예수금:%-7s | 평가자산:%-7s  원금:%-7s 수익금:%-7s 수익율:%-5s %%" \
        #     % (str_price , str_change_ratio, action, quantity, sum_quantity, str_average_price,str_evaluation_price, str_cash, str_asset, str_principal_price, str_income, str_ratio))
        print("%-6s %9s  %-2s %4s  %7s %8s %7s | %9s   %8s |%12s  %10s %9s %5s %% %s" \
            % (str_price , str_change_ratio, action, str(quantity), sum_quantity, str_average_price, \
                str_average_price_ratio, str_evaluation_price, str_cash, str_asset, str_principal_price, str_income, str_ratio, comment ))
        index = index + 1

    print("=========== 요약정보==========")
    print("시작금액:%s 종료금액:%s" %( "{:,}".format(first_price), "{:,}".format(last_price)))
    print("가격변동:%3.2f %%" %(tool.getFluctuationRatio(first_price, last_price)))

#=====================================================================================================    
main()

# lst = [1000, 1100, 1200, 1300]
# idx = tool.canSell(1000, lst, 1)
# print(lst)
# print("index:%d" %(idx))










