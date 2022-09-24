from __future__ import annotations #type hint
from typing import Any,Type
import hashlib
import random
class Hash_node:
    """ 해시 노드"""
    
    def __init__(self,key=None,value=None) -> None:
        self.key=key
        self.value=value
        self.next =None
        
    def __del__(self):
        pass
    def set_(self,key,value,next=None,):
        self.key=key
        self.value=value
        self.next=next
        # self.before=before
        
class  Hash_head:
    """" 헤드포인터 """
    #헤드의 속성으로는 class hash_node를 가져야한다
    def __init__(self,capacity=5):
        self.capacity=capacity
        self.table=[None for _ in range(capacity)]
        for i in range(capacity):
            self.table[i]=Hash_node()
            
    def hash_value(self,key):
        """해시값을 구한다"""
        if isinstance(key,int):  #key값이 int형인지 확인합니다
            data=key%self.capacity
            return data

        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        #key 값이 int형이 아닐시 hashlib를 이용하여 incoding을 한다

    
    def set_hash(self,key,value):
        data=self.hash_value(key)
        back_tracking=self.table[data] #루프의 NEXT의 한단계를 추적한다
        if self.table[data]==None:  #키값할당하기전에 객체가 DEL연산자로 전부다 삭제되버리면 다시 객체를 재할당해준다
            self.table[data]=Hash_node()
        roop=self.table[data].next #루프시작을 한노드의 NEXT포인터로 잡는다
        
        while roop is not  None: #HASH_NODE의 NEXT가 NONE이 아닐동안 반복합니다
            roop=roop.next
            back_tracking=back_tracking.next
        if self.table[data].key ==None: #해당버킷에 링크드리스트가 존재하는가?
            self.table[data].set_(key,value)
        else:
            back_tracking.next=Hash_node(key,value) 
            
    def serach(self,key,value)->any:  #사용자가 key값을 입력하시 value를 return 한다
        data=self.hash_value(key)
        roop=self.table[data]
        count=0
        while roop  is not None:
            if roop.value==value:
                print("hash_table {}번쨰에 저장되어있으며 링크드{}순위에있으며 {}를찾았습니다"
                      .format(data,count,value))
                return data,value,count
            count+=1
            roop=roop.next
        return False
    def remove(self,key,value)->bool:
        """ 사용자가 key값을 입력후 해당value를가진 링크드 삭제 """
        data=self.hash_value(key)
        back_tracking=None
        roop=self.table[data]
        while roop is not None:
            if roop.value==value:
                print("hash_key값이 {}인 value={}를 삭제합니다".format(data,value))
                """
                back_tracking을 그다음 next로 연결해야한다 그러나 예외사항이 존재
                1) 만약 back_tracking이 None이라면 삭제대상이 처음대상이므로 연결이아닌 단순삭제
                """
                if back_tracking==None:
                    self.table[data]=self.table[data].next
                    del roop #소멸자 호출 정상작동...??????
                    self.all_print_elem()
                    print("")
                    return True
                back_tracking.next=roop.next #추적의 다음링크를 삭제대상 그다음 링크로 연결시킨다
                del roop # roop 삭제
                print("")
                self.all_print_elem()
                return True
            back_tracking=roop
            roop=roop.next
        
        print("삭제 대상 서칭 실패")
        return False
    def all_print_elem(self):
        for i  in range(self.capacity):
            roop=self.table[i] #수정대기 소멸자 발생시 NONE발생 
            print("{} ---->".format(i),end='')
            if roop==None:
                print("(미지정)")
                continue
            if roop.value==None:
                print("(미지정)")
            else:
                while roop !=None:
                    print("{} ".format(roop.value),end='')
                    roop=roop.next
                    if roop!=None:
                        print("->",end=' ')
                print()
            
               
    
                
        
        

    
if __name__=="__main__":
    H1=Hash_head(10) #해시용량 defalut 5
    H1.set_hash(10,"test")
    H1.set_hash(10,"simple")
    H1.set_hash(10,"Data structures")
    H1.serach(10,"test")
    H1.serach(10,"simple")
    H1.serach(10,"Data structures")
    H1.remove(10,"kello")
    H1.remove(10,"test")
    H1.remove(10,"Data structures")
    H1.remove(10,"simple")
    for i in range(100):
        random_=random.randrange(0,100)
        input_data=random.uniform(0,10)
        H1.set_hash(random_,round(input_data,2))
        
    H1.all_print_elem()

    
        