import glob 
import os
import time
import datetime
print(glob.glob("*py"))
print(os.getcwd())

folder="sample_dir"

if os.path.exists(folder):
    print("이미존재하는 풀더")
    os.rmdir(folder)
    print(folder,"폴더 삭제")
else:
    os.makedirs(folder)
    print(folder,"풀더를 생성")
print(os.listdir())#glob.glob
print(time.localtime())
print(time.strftime("%Y-%m-%d %H %M %S"))


print("오늘 날짜는",datetime.date.today())

today=datetime.date.today()

td=datetime.timedelta(days=100)

print("우리가만난지",today+td)

