"""
문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.
"""

buffer={'c':1,'d':2,'e':3,'f':4,'g':5,'a':6,'b':7,'C':8}
user=list(map(int,input().split())) #사용자로부터 8개의 숫자를 입력 map input str map map메모리주소
if user==sorted(user): #더좋은방식
    print("ascending")
elif user==list(reversed(sorted(user))): 
    print("decending")
else:
    print("mixed")

# test_ascending=list() 
# test_decending=list()
# # 1 5 3 7 -> 1 3 5 7
# test_ascending=sorted(user) #사용자로부터 입력받은 8개의값을 저장한 리스트 sorted(list)오름차순으로 list에서받아서 반환을 list
# test_decending=list(reversed(sorted(user))) #reversed 메모리주소 revese object at 메모리주소
# print(list(reversed(sorted(user)))) #list.sort sorted
# list.sort ->원본데이트 sort바뀜 
# reverse(sorted(list)) ->원본데이터변경x 새로운 list반환
# user==test_decending 메모리주소 달라여 다른 객체이죠

# if user==test_ascending: #오름차순으로 정렬된거랑 사용자가입력한것이 같으면
#     #8개만 소유시간 x 100개 100개 1000개     user.index(i)==test.index(i)
#     print("ascending") #오름차순으로 입력한것이고
# elif user==test_decending: #사용자가입력한것이 내림차순으로 
#     print("descending")
# else:
#     print("mixed")
