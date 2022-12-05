import random
a = [ random.randrange(20)  for i in range(10)]

for i in range((len(a)-1),-1,-1):
    target = i
    target_c = ( target * 2 ) + 1
    
    if target_c >= len(a): # ??X
        pass
    
    else: # ??? ????????
        if target_c+1 < len(a):
            if a[target_c] < a[target_c+1]:
                target_c+=1
                
        if a[target_c] > a[target]:
            a[target] , a[target_c] = a[target_c] , a[target]
            
            
    
    while target !=0:
        target_p = (target-1)//2
        if a[target_p] < a[target]:
            a[target] , a[target_p] = a[target] ,a[target_p]
            
        target = target_p
        
print("Max_Heap",a)
        
            

        


