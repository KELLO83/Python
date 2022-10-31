#사용자에게 입력을받고 2진 8진 16진을 구하여라 단 재귀 사용

def convert_sec(n):
    if n//2==0:
        return str(n%2)
    return convert_sec(n//2)+str(n%2)

def convert_octal(n):
    if n//8==0:
        return str(n%8)
    return convert_octal(n//8)+str(n%8)

def convert_Hex(n):
    if n//16==0:
        if n>=10:
            n=n-10
            tmp=chr(65+n)
            return str(tmp)
        return str(n)
    tmp=n%16
    if tmp>10:
        tmp=tmp-10
        tmp=chr(65+tmp)
    return convert_Hex(n//16)+str(tmp)
            
user=int(input())
print(convert_sec(user))
print(convert_octal(user))
print(convert_Hex(user))