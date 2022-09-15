import os
import glob
file="practice_dir"

if os.path.exists(file):
    print("이미 {0}가존재한다".format(file))
    os.rmdir(file)
    print(file,"삭제완료")
    
else:
    os.makedirs(file)
    print(f"{file} 생성완료")
    
    
print(os.getcwd())



print(os.listdir("C:\\python\\module"))

print(os.listdir("C:\\python\\library"))




print(glob.glob("C:\python\module\*.py"))

print(glob.glob("C:\python\library\*.py"))

