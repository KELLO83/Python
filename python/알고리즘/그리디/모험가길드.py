
N = int(input())
Member = list(map(int,input().split()))
save_people = list()
Member.sort()

print(Member)
Grop_count = 0

for i in range(len(Member)): 
        save_people.append(Member[i]) # 1 2 2 3 8
        if len(save_people) >= max(save_people): # [2,2] 2 clear [] 
            Grop_count +=1
            save_people.clear()
            



print(Grop_count)        
        
    
