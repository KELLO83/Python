list_=['a','b','c']
#순서쌍으로 tuple형태로 출력 idex가 붙은형태로 출력
for i  in enumerate(['a','b','c']):
    print(i)
    
    
# unpacking

for i,v in enumerate(list_):
    print(i,v)
    
# index 번호 시작지점 정하기

for i,v in enumerate(list_, start=10):
    print(i,v)