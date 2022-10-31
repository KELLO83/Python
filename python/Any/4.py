word=input().upper()

s=list(set(word))

hw=[]

for i in s:
    hw.append(word.count(i))
print(hw)
m=max(hw)
print(m)

