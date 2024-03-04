from __future__ import annotations
from typing import Any, Type
import hashlib

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


class Hash_Node(object):
    def __init__(self,key,value) ->None:
        self,key=key
        self.value=value
    def __del__(self):
        pass
    def set_(self,key,value):
        self.key=key
        self.value=value

class Opening_Hash():
    def __init__(self,capacity=5):
        self.capacity=capacity
        self.table=[None for  _ in range(capacity)]
        for i in range(capacity):
            self.table[i]=Hash_Node() #메모리할당
    
    def hash_value(self,key):
        if isinstance(key,int):  #key값이 int형인지 확인합니다
            data=key%self.capacity
            return data
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def set_hash(self,key,value):
        data=self.hash_value(key)
        if self.table[data].key==None and self.table[data].value==None:
            self.table[data].key=key
            self.table[data].value=value
        #해당 버킷리스트에 데이터가 들어가있다 그뒤한칸에저장 거기도저장되어있으면 그다음... 무한
        #종료조건: 버킷이 max일경우 hash resizing필요
        else:
            roop=data
            roop+=1
            while roop<len(self.table)-data: # 2가 자리없어서 3시작 4시작 5시작  전체크기 5 -3=2  검증필요
                if self.table[roop].key==None and self.table[roop].value==None:
                    self.table[roop].key=key #주의사항 원래키값이 들어가할 버킷자리가 아니다!!
                    self.table[roop].value=value
        print("해시 테이블의 버킷자리가 max입니다 해시 resize가 필요합니다")
        return False
    
    def find_slot(self,key):
        data=self.hash_value(key)
        start=data
        if  self.table[data].key==key:
            return data #return find_slot
        else:
            data+=1
            while data==start:
                #while문과 if문이 끝나는 경우 
                # 1.Hash_table에 empty가있을경우
                # 2.Hash_table  full상태이지만 find key를 했을경우
                data=(data+1)%len(self.table)
                if self.table[data].key==key:
                    return self.table[data]
                if self.table[data].key==None:
                    return False
                # if self.table[data].key==key:
                #     return data #return find_slot
                
    def serach(self,key,value):
        res=self.find_slot(key,value)
        if res!=False:
            print("{} 번쨰슬롯에 value {}가 저장되어있습니다".format(key,value))
            return True
        print("검색 실패")
        
    def remove(self,key):
        current_slot=self.find_slot(key)
        find_slot=current_slot+1
        if self.table[current_slot].key==None:
            print("삭제 대상이 없습니다")
            return True
        elif self.table[current_slot].key==key:
            print("삭제를 진행합니다")
            del self.table[current_slot]
            self.table[current_slot]=Hash_Node()
            return True
        while True: #루프의 범위 find_slot==current_slot
            if (self.table[find_slot]).key==key:
                print("삭제를 진행합니다")
                del self.table[find_slot]
                return True
            
            find_slot=(find_slot+1)%self.capacity  #용량 5 현재 2 이동 3 => 2 슬롯 
            if(find_slot==current_slot):
                print("해당 {}값을 가진 슬롯을 발견하지 못했습니다".format(self.find_slot(key)))
                return False
            
            
        
            
            
            