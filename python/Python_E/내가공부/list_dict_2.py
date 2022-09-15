import sys

a=dict()

a[1]="hello"
a[2]="love"
a[3]='python'


# print(a)


# for key in a:
#     print(key)    
    

# if  '1' in a:
#     print("True")
    
    
# for key,value in a.items():
#     print("key {} value{}".format(key,value))


grade={'pey':10,"julliet":99}


temp=grade['pey']=20
print(temp)

del grade['pey']

print(grade)

print(grade.keys())


grade['kello']="Kb bank"

print(grade['kello'])


print(grade.keys())

print(grade.values())



grade.clear()

print(grade)

grade[153]="dsabn"

print(grade.get(153))

if 'dsabn' in grade.values():
    print('True')
else:
    print('FALSE')
    
    
    
    
    


n1=sys.stdin.readline()
print(n1)



