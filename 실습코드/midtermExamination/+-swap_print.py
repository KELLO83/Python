# +와-를 반복하며 출력하기
#i가홀수면 -를 출력
#i가짝수면 +를 출력
def orgin(count):
    for i in range(count):
        if i%2==0:
            print("+",end=" ")
        else:
            print("-",end=" ")
    print()

def imporving(count):
    
    for i in range(count//2):
        print("+ -",end=" ")

    #사용자에게 입력한값이 홀수일시 +로끝남
    #짝수일시 -로끝난다
    
    if  count%2!=0:
        print("+",end=" ")
    print()        
#*을 n개마다 출력하되 w개마다 줄바꿈
# 3개마다 줄바꿈한다면?? 10개 input 4찍을때 줄바꿈해야됨
def inline(star,line_enter):
    for i in range(star):
        print("*",end="")
        
        if i%line_enter==line_enter-1: ###?????? 
            print()
             
    if star%line_enter:
        print()
        
def user_inline(star,line_enter):
    for i in  range(star):
        print("*",end="")
        if i%line_enter==line_enter-1:
            print()
            
    if star%line_enter:
        print("")
    
    print("debug")
        

if __name__=="__main__":
    # orgin(6)
    # imporving(6)
    user_inline(15,5)