with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("hello world")
    

with open("study.txt","r",encoding="utf8") as study_file:
    temp=study_file.read()
    print(temp)
    
    
with open("test.txt","w",encoding="utf8") as list:
    list.write("kello")
    
with open("test.txt","r",encoding="utf8") as list_file:
    print(list_file.read())    

    
        