import collections

data=collections.OrderedDict()

data['hello']=1
data['hi']=3
data['word']=2


print(data)

if 'hi' in data:
    print("hi in dict.key") #key가 있는지검사
    
for key in data.keys():
    print(key) #key만 추출하기

for value in data.values():
    print(value) #value만 추출하기

for key,value in data.items():
    print(key,value) #모든 요소추출하기

def get_score(name,**kwargs):
    print(name)
    total=0
    for i in kwargs.values():
        total+=i
    print(f"총합은 {total} 입니다")
    for i in kwargs.keys():
        print("수강한과목은 {}입니다".format(i))

get_score('kello',en=80,ko=30,math=100)



