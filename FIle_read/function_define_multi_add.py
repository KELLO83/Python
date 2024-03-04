

def add_mul(choice,*argument):
    if choice=="add":
        result=0
        for i in argument:
            result=result+i
        return result        
    elif choice=="mul":
        result=1
        for i in argument:
            result=result*i
        return result       
                
            
            
result_multi=add_mul("mul",1,2,3,4,5)
print(result_multi)


result_add=add_mul("add",1,2,3,4,5)
print(result_add)

