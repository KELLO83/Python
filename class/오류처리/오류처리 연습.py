try:
    print("나누기 전용계산기")
    n=[]    
    n.append(int(input("첫번째 숫자입력")))
    n.append(int(input("두번째 숫자입력")))
    # n.append(n[0]/n[1])
    
    print ("{0}/{1} = {2}".format(n[0],n[1],n[2]))

# except ValueError:
#     print("value error err")
except ZeroDivisionError:
    print("zero division error err")

except Exception as err:
    print("unknown error err")
    print(err)
        
    
    
        
    
    