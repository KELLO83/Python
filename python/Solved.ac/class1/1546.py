import statistics
def convert(n):
    return round(n/max_score*100,5)

count=int(input()) #사용자로부터 입력받는 과목의 수
score=list(map(int,input().split())) #공백을 기준으로 성적입력 list형태로 받는다
max_score=max(score)
score=list(map(lambda x: round(x/max_score*100,10), score))
print((statistics.mean(score)))


test=list(map(convert,score))
print("수정데이터",test)

