# score_file=open("score.txt","w",encoding="utf8")
# print("수학:0",file=score_file)
# print("영어:50",file=score_file)

# score_file.close()


# score_file=open("score.txt","a",encoding="utf8")
# score_file.write("과학=80")
# score_file.write("\n코딩=100")#ㅈ줄바꿈 지원 x

# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")

# print(score_file.read())
# score_file.close() 한번에 읽기


score_file=open("score.txt","r",encoding="utf8")

lines=score_file.readlines()#list 형태로 저장
for line in lines:
    print(line,end="")
    


score_file.close()#printf는 자동 줄바꿈
