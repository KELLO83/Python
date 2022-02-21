def readData(filename, pricelist):
    f = open(filename)
    while True:
        line = f.readline()
        if not line: break
        value = line.strip()
        intValue = int(value)
        pricelist.append(intValue)
    f.close()

def canSell(current_price, list_bought_price, riseRatio ):    
    index = -1
    idx = 0;
    targetPrice = current_price + ( current_price * riseRatio / 100 )
    for boughtPrice in list_bought_price:        
        if boughtPrice < targetPrice:
            index = idx         
            # print("currentPrice:%d boughtPrice:%d targetPrice:%d" %( current_price, boughtPrice , targetPrice))
            break   
        idx = idx + 1
        
    return index

def removeSell(current_price, list_baught_price, riseRatio):
    index = canSell(current_price, list_baught_price, riseRatio)
    result = 0
    if index > -1:
        value = list_baught_price[index]
        list_baught_price.remove(value)
        result = value
    return result
        
def setRed(text):
    #return text
    return '\033[38;2;255;0;0m' + text + '\033[0m'

def setBlue(text):
    #return text
    return '\033[38;2;0;255;0m' + text + '\033[0m'

def setYellow(text):
    #return text
    return '\033[38;2;255;255;0m' + text + '\033[0m'

#prinipal : 원금 , evaluation_price : 현재금액
def getFluctuationRatio(principal, evaluation_price ):
    try:
        income  = (evaluation_price - principal)  # 수익금 = 자산금액 - 원금
        ratio   = (income / principal) * 100 #수익율
        return ratio
    except:
        return 0
