#Hash table
#매우빠른 평균 삽입 삭제 탐색 연산 제공
#Table: list
#Hash function ->mapping
#collision resolution method

#충돌회피 방법을 사용해야한다
#1.opena ddressing 출돌일어날시 주위의 빈칸을 찾아서 그곳에 저장을시킨다
    #limear probling 
    #qudrating probing
    #dobule Hasing
#2.chaining addresing

#limear probling 
#충돌일어날시 바로밑에다가 데이터삽입 거기도 차있을시 밑으로... 아래빈칸에다가 데이터삽입


#Hash function //10
#10개의 hash table circle list

class Hash(object):
    def __init__(self):
        self.Hash_table=[None for _ in range(10)] #10칸의 hash table
       
    def search(self,key): #작성필요 key값을줄시 해당 hash의 value를 리턴한다
        pass
    
    def set(self,key,value=None): 
        #key 값이 h에 있으면 value를 update
        #key 값이 H에 없으면 (Key,value)을 insert
        i=self.find_slot(key)
        value=self.Hash_function(key)
        if i==False:
            print("Hash talbe full Not find key")
            #Hash_table의 용량을 증가시켜야한다 저장할공간이 없기떄문에->만들어야함
            return False #실패
        else:
            if self.Hash_table[i]!=None:
                self.Hash_table[i]==value #key값 업데이트 기존에있던값대신 새로운값을 넣는다
                return value
            
            elif self.Hash_table[i]==None: #Hash_table[i]에 값이 엀을경우
                self.Hash_table[i]=value
                return value   
                



    def remove(self,key):
        i=self.find_slot(key)
        if self.Hash_table[i]==None: #삭제할 value가 존재하지않는다
            return None
        else: 
            j=i
            while True:
                self.Hash_table[i]=None #지우자고하는 해당 slot의 value를 삭제한다
                while True: #hash떙기기
                    j=(j+1)%len(self.Hash_talbe)
                    if self.Hash_table[j]==None:
                        return key
                    else:
                        k=self.Hash_function(key)
                        
                        if (k<i<=j) or (i<j<k) or (j<k<i):
                            break
                        
                self.Hash_table[i]==self.Hash_table[j]
                i=j
                

            
    
    def find_slot(self,key):  #완성
        #key값이 있으면 slot번호 리턴 없으면 그 key값이 삽입될 slot 번호를 return한다
        i=self.Hash_function(key) #Hash function
        start=i
        while self.Hash_table[i]!=None: 
            #while문과 if문이 끝나는 경우 
            # 1.Hash_table에 empty가있을경우
            # 2.Hash_table  full상태이지만 find key를 했을경우
            if self.Hash_table[i]!=key:
                i=i+1%len(Hash_table)
                if i==start:#한바퀴 다돌음
                    return False #Hash_table이 full 이다
            elif self.Hash_table[i]==key:
                print("find key break")
                break
        return i #i=Hash_table의 슬롯 번호
    
    def Hash_function(self,value):
        value=value%10
        return value
        
        
            
if __name__=="__main__":
    hash=Hash()
    hash.set(5)