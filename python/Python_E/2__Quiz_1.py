#정수를 입력받고 짝 홀 판단하라

number=int(input("정수를 입력하세여"))

if number%2==False:
    print(f"짝수입니다 {number}")
else:
    print(f"홀수입니다 {number}")

if not bool(number%2):
    print("짝수")
else:
    print("홀수")
