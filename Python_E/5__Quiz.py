#재귀함수를 이용하라
#a1=1
#a2=1
#a3=2
#a4=3
#a5=5

# number_2=None #기준점에 두번뒤의 숫자 -2 칸느림
# number_1=None #기준점에 한번뒤의 숫자 -1 칸느림
# loop=int(input("반복횟수 입력"))
# loop_count=0
# def call():
#     global loop_count
#     global number_1
#     global number_2
#     if loop_count==0:
#         number_1=1
#         number_2=None
#         print("{}".format(1))
#         loop_count+=1
#         if loop_count==loop:
#             return None
#         call()
#     elif loop_count==1:
#         number_2=1
#         number_1=1
#         print("{}".format(1))
#         loop_count+=1
#         if loop_count==loop:
#             return None    
#         call()
#     else:
#         result=number_1+number_2
#         print("{}".format(result))
#         number_1=number_2
#         number_2=result
#         loop_count+=1
#         if loop_count==loop:
#             return None
#         call()
    

# if __name__=="__main__":
#     call()
    
    
# loop=int(input("반복횟수"))
# loop_count=loop
# def call(loop,number_1,number_2):
#     global loop_count
#     if loop==False:
#         return None
#     if loop_count==loop:
#         print("{}".format(1))
#         test=call(loop-1,number_1=1,number_2=None)
#         if test==None:
#             return None
#     if loop_count-1==loop:
#         print("{}".format(1))
#         test=call(loop-1,number_1=1,number_2=1)
#         if test==None:
#             return None
#     else:
#         result=number_1+number_2
#         print("{}".format(result))
#         number_2=number_1
#         number_1=result
#         test=call(loop-1, number_1, number_2)
#         if test==None:
#             return None


#재귀함수를 이용하라
#a1=1
#a2=1
#a3=2
#a4=3
#a5=5


loop=int(input("반복횟수 입력하세요"))
def call(loop):
    if loop<=2:
        return 1
    else:
        return call(loop-1)+call(loop-2)
if __name__=="__main__":
    call(loop)