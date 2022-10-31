#오른쪽 아래가 직각인 이등변삼각형을 출력하자

n=int(input("삼각형의 높이를 정하세요"))

"""
    *
  * *
* * *

3개짜리별이라면 처음 2칸띄고 2번째 한칸 마지막 안뜀
"""
for i in range(n):
    for _ in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    
        
        
        