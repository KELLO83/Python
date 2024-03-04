
user=input()
ck_set=set(user.upper())
ck_list=list(user.upper())
ck_dict=dict()

for i in ck_set:
    tmp=ck_list.count(i)
    ck_dict[i]=tmp
try:
    del(ck_dict[' '])
except:
    pass



res=[k for k,v in ck_dict.items() if max(ck_dict.values())==v]
if len(res)>1:
    print("?")
else:
    print(''.join(res))