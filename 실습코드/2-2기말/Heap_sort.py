import random
data = [ random.randrange(20)  for i in range(10)]
print("초기 생성",data)

for i in range(len(data)-1,-1,-1):
    target =i
    target_c = (target *2 )+1
    
    if target_c>=len(data):
        pass
    else:
        if target_c+1 >= len(data):
            pass
        else:
            if data[target_c] < data[target_c+1]:
                target_c+=1
                
        if data[target] < data[target_c]:
            data[target] , data[target_c] = data[target_c] , data[target]
            
    
    while target !=0:
        target_p = ( target-1 ) //2
        
        if data[target_p] < data[target]:
            data[target] , data[target_p] = data[target_p]  ,data[target]
            
        target = target_p    
        
        
print("MAX_HEAP구성",data)


for i in range(len(data)-1,-1,-1):
    data[0],data[i]= data[i],data[0]
    
    root = 0
    
    while root *2 +1 < i:
        child = (root*2)+1
        if child+1 >= i:
            pass
        else:
            if data[child] < data[child+1]:
                child+=1
        
        if data[child] > data[root]:
            data[child ] , data[root] = data[root] , data[child]
            
        root = child   
         
print("힙정렬완료",data)