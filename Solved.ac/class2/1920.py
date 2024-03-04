user_input=int(input())
data=list(map(int,input().split()))
data=data[:user_input]

ck_input=int(input())
ck=list(map(int,input().split()))
ck=ck[:ck_input]

data.sort()


for i in ck:
    start=0
    last=len(data)-1
    
    while True:
        middle=(start+last)//2
        
        if data[middle]==i:
            print("1")
            break
            
        elif data[middle]<i:
            start=middle+1
        else:
            last=middle-1
        
        if start>last:
            print("0")
            break