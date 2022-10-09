arr=[1,2,3,4]

f=lambda x:x*2
print(list(map(f,arr)))

arr2=[10,20,30,40]

f=lambda x,y:(x*2,y*2)

print(list(map(f,arr,arr2)))


arr=[1,2,3,4,5,6,7,8,9]

f=lambda x:True if x%2==0 else False
print(list(filter(f,arr)))