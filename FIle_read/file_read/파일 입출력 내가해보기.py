name_list_file=open("name.txt","w",encoding="utf8")

print("dsban",file=name_list_file)
print("kello",file=name_list_file)
print("hello",file=name_list_file)

temp="string"

name_list_file.write(temp)
name_list_file.write("winter is cool")
name_list_file.write("\nhello world")

name_list_file.close()


list=open("name.txt","r",encoding="utf8")

line=list.readline()

print(line)

print(list.readline())

while True:
    line=list.readline()
    if not line:break
    print(line)
    
list.close()

print("다시 파일 오픈")

list_name_file=open("name.txt","r",encoding="utf8")

print(list_name_file.readlines())

list_name_file.close() 

print("파일 read사용해보기")

name=open("name.txt","r",encoding="utf8")

print(name.read())

##파일 쓰기에는 print를 이용한 쓰기 및 write를 이용한 쓰기
#파일 읽기에는 readline을 이용한 한줄씩 따오기 자동 줄바꿈
#readlines이용하여 리스트의 혈태로 따오기
#read를사용하여 가져오기 줄바꿈 지원x


 
    
    
        

