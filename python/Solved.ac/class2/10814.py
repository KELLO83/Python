user=int(input())
data_base=list()
regist=list()
for i in range(user):
    age,name=input().split()
    data_base.append((int(age),name))
    regist.append((int(age),name))
    
data_base.sort()

print(data_base)

