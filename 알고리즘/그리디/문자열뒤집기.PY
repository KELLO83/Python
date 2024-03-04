#  110011110000000000000 --> 1010
s = list(map(int,input()))
buffer = list()
start_location = 0
# print(s)

for i in s:
    start = s[start_location]
    for j in range(start_location,len(s)):
        if start == s[j]:
            pass
        else:
            buffer.append(start)
            start_location = j
            break
buffer.append(s[len(s)-1])
# print(buffer)

zero = buffer.count(0)
one = buffer.count(1)


if zero < one:
    print(zero)
else:
    print(one)