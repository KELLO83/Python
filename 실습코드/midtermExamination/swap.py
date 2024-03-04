print("a부터 b까지의 합을 구합니다")
a=int(input("input a"))
b=int(input("input b"))

if a>b:
    a,b=b,a #swap
    
sum=0
3
for i in range(a,b+1):
    sum+=i
    
    
print(f"{a} 부터 {b} 까지의 합은 {sum} 입니다")