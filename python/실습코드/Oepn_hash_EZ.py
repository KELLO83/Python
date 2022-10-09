from __future__ import annotations
from typing import Any,Type
from enum import Enum
import hashlib


class Status(Enum):
    OCCUPIED=0
    EMPTY=1
    DELETED=2
    
class Bucket:
    def __init__(self,key=None,value=None,Status=Status.EMPTY) -> None:
        self.key=key
        self.value=value
        self.Status=Status
        
    def set(self,key,value,Status=Status.OCCUPIED)->None:
        """ Bucket에 key,value를 추가합니다 status상태 변경"""
        self.key=key
        self.value=value
        self.Status=Status


class OpendHash:
    def __init__(self,capacity=10) -> None:
        self.capaicty=capacity
        self.Hash_table=[Bucket()]*self.capaicty
    
    def Hash_Key(self,key):
        """ 사용자가입력한 key값을 Hash key값으로 변환합니다"""
        if isinstance(key,int):
            return key%self.capaicty                     
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)
        
    def add(self,key,value):
        """ 사용자로부터 key와 value를 받아서 Bucket에 추가한다"""
        Hash_key=self.Hash_Key(key)
        for i in range(self.capaicty):
            if self.Hash_table[Hash_key].Status==Status.OCCUPIED: #조정필요
                Hash_key=(Hash_key+1)%self.capaicty
                continue
                
            elif self.Hash_table[Hash_key].Status!=Status.OCCUPIED:
                self.Hash_table[Hash_key]=Bucket(key,value,Status.OCCUPIED)
                return True
        return False #삽입실패
    
    
    def DEBUG(self):
        """해시테이블의 갯수와 원소 상태를 조사합니다"""
        print("DEBUG")
        for i  in range(self.capaicty):
            print("{} key={} value={}".format(i,self.Hash_table[i].key,
                                              self.Hash_table[i].value))
        print("DEBUG")
        
        
if __name__ =="__main__":
    H1=OpendHash()
    H1.add(15,"kello")
    H1.add(25,"JELLO")
    
        
    