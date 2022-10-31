arr=[[1,2,3],[4,5,6],[7,8,9]]
res=list()
buffer=list()

for i in list(zip(arr[0],arr[1],arr[2])):
    res.append(list(i))
    
print(res)

for i in list(zip(*arr)):
    buffer.append(list(i))
    
    
print(buffer)