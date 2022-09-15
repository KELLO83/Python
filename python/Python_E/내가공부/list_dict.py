

import numpy


arr2=['1',2,["I LOVE","pyhton"]]

for i in range(3):
    print(arr2[i])
    
print(arr2[2][0])
print(arr2[2][1])


print(type(arr2[0]))


print(arr2[2][0]+(arr2[0]))


Array_=[1,2,3,['a','b',3],[5,6]]


print(Array_)

print(Array_[3][2]+Array_[4][1])


numpy_=[1,2,3]

print(dir(arr2))


print(numpy_.__add__(numpy_))

# if 3 in numpy_:
#     print("True")
    
# if  ['pyhton'] in arr2:
#     print("True")
# else:
#     print("False")


# odd=[i**2 for i in range(10) if(i%2==1)]

# print(odd)

# odd__1=odd

# print(odd__1)

# odd__1[0]=False
# print(id(odd),id(odd__1))

# print(odd)

# odd__2=odd[:]

# print(id(odd__2))

# kel=odd.copy()

# print(id(kel))

# print(odd__2 is odd)


key={1:"hi",2:"bye","python":"love"}


print(key["python"])

key[3]="third"

print(key[3])

print(key)


del key[3]

print(key)


key[(1,2,3)]=[1,2,3,4,5]

print(key[(1,2,3)])

key.keys

a={1:'one',2:'two'}


print(a.items())