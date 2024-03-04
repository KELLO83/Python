import collections

data=collections.OrderedDict()

data['d']=100
data['b']=300
data['a']=200
data['c']=400

for i,j in data.items():
    print(i,j)
    
print(sorted(data.keys())) #keys에 의한 정렬
print(sorted(data.items())) #items에 의한 정렬 key값의 사전순으로 sorted된다
print(sorted(data.values())) #value에 의한 정렬

#딕셔너리의 key의 value에 기본값을 지정하는 방법

data=collections.defaultdict(lambda:0)
print(data)
    