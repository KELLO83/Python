
class bit_find():
    def __init__(self):
        self
    def bit_check(self,bit_array,bit_number,bit_range): #bit_array 는 내가 궁금한 n번쨰 비트의 자릿수를 지정한다 bit_number는 0인지 1인지 인수를 받는다 bit_ragne 0부터 ~bit_ragne까지의 2진수를 저장후 해당사항을 전부찾는다
        
        bit_list=list()
        for i in range(int(bit_range+1)):
            bit_list.append(str(bin(i))) #bit_range ex)15입력시 10진수 0~15까지의 10진수를 bit_list에 2진수으로 저장한다
            
        print("{}범위내 2진수는 {}입니다".format(bit_range,bit_list))
        
        bit_divison=list() 
        result=list()
        clear_bit_list=self.del_b0(bit_list)
        s2=str()
        print("0b를 삭제한 bit_list= {}입니다".format(clear_bit_list))
        for i in clear_bit_list:
            s1=i[len(i)::-1] #bit_list 에있는 각 문자열을 뒤집은채로 저장한다 밑에있는 if문의 bit_array번째칸의 비트가 0인지 1인지 판별하기위해서... ex)0b11를 11b0로 저장하는것..
            try:
                s2=s1[bit_array-1]
                if s2==str(bit_number):
                    result.append(i)
            except:
                pass
        else:
            pass #bit_array 번째가 bit_number의 수가 아닐경우 저장하지않고 넘어간다
        
        print("{} 번쨰 비트가 {}인 모든 {} 범위내 2진수는 {}입니다".format(bit_array,bit_number,bit_range,result))
        trans_=self.ten_tras_(result)
        print("해당하는 2진수 {} 의 10진수의 값은 {} 입니다".format(result,trans_))
        return result
    
    def ten_tras_(self,list_): #2진수의 리스트를 해당하는 10진수의 값이 무엇인지 궁금할때 사용한다
        reset_2bit=list()
        temp=int()
        for i in list_:
            bit_set=len(i)
            for j in i:
                if j=='1':
                    temp=temp+(2**(bit_set-1))
                bit_set-=1
            reset_2bit.append(temp)
            temp=0
        return reset_2bit
            
    def del_b0(self,list_): #쓸모없는 bo를 제거한 리스트를 리턴한다
        del_b0_list=list()
        for i in list_:
            s1=i[2:]
            del_b0_list.append(s1)
            
        return del_b0_list
            
if __name__=="__main__":
    b=bit_find()
    b.bit_check(3, 1,15)

    # b.bit_check(3,0, 20)
    #0->0b0
    #1->0b1
    #2->0b10
     
    # 0b10 0b11 0b110 0b111 0b1010 0b1011 0b1110 7가지 10진수 2 3 7 10 11 14  
    
    # 1부터 15 이진수 ['0b0', '0b1', '0b10', '0b11', '0b100', '0b101', '0b110', '0b111', '0b1000', '0b1001', '0b1010', '0b1011', '0b1100', '0b1101', '0b1110']