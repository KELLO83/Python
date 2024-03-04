#4주차 강의 

#for 문 for 반복변수 in range(횟수)
# for i in range(5) 0 1 2 3 4 ..
# for i in ragne(시작 숫자,끝 숫자) range(2,5) 2 3 4 3번


# for i in range(2,10):
#     for j in range(1,10):
#         print("%d*%d =%d"%(i,j,i*j))
    
#     print("\n")
    
#while 문 while (조건):
#whil 참일떄 -> 1.True 2.0이외의 수 3.공백이아닌리스트 

# while True:
#     n1=int(input("정수를입력하세여"))
#     if n1%2==0:
#         print("짝수")
#     else:
#         print("홀수")
        
#while break 문과 continue문 continue문은 아래에있는문장들을 무시하고 다시 반복문으로 돌아간다

# for i in range(10):
#     if i%2==0:
#         continue
#     print("%d 홀수입니다"%i)


n1=int(input("정수를입력하세여"))
reuslt=0
for i in range(1,n1+1):
    
    if i%2==0:
        reuslt+=i
    else:
        pass
    
print("입력 받은 모든 짝수의 정수들의 합은 %d입니다"%reuslt)



