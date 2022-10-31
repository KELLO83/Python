#사용자로부터 10진수를 입력받아 2진수 8진수 16 변환을하여라

def convert_second(user:int):
    if user<2:
        return str(user)
    else:
        return convert_second(user//2)+str(user%2)


def convert_octal(user:int):
    if user<8:
        return str(user)
    else:
        return convert_octal(user//8)+str(user%8)

def convert_Hex(user:int):
    if user<16:
        if user<10:
            return str(user)
        else:
            return str(chr(65+(user-10)))
    else:
        tmp=user%16
        if tmp>=10:
            tmp=chr(65+(tmp-10))
        return convert_Hex(user//16)+str(tmp)
    

if __name__=="__main__":
    user=int(input("10진수입력"))
    print(convert_second(user))
    print(convert_octal(user))
    print(convert_Hex(user))