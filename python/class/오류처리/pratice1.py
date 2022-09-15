
try:
    a=[1,2,3,4]
    
    a.pop()
    a.pop()
    a.pop()
    a.pop()
    a.pop()


    
except ZeroDivisionError:
    print("제로 에러")
    
except ValueError:
    print("value erorr")
        
except IndexError:
    print("Index Error err")
except Exception as err:
    print(err)
    
finally:
    print("오류검사 완료")
    
    