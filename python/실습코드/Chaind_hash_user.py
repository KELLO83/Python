from __future__ import annotations
from typing import *
import hashlib

class Node:
    def __init__(self,key,value,next):
        self.key=key
        self.value=value
        self.next=next
class ChainedHash:
    
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.Hash_table=[None for _ in range(self.capacity)]
        
    def hash_value(self,key):
        if isinstance(key,int):
            return key%self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
     
    def add(self,key,value):
        hash=self.hash_value(key)
        target=self.Hash_table[hash]
        
        while target is not None:
            if target.key==key:
                print("이미추가돤 key값입니다") 
                return False
            target=target.next
        temp=Node(key,value,self.Hash_table[hash])
        self.Hash_table[hash]=temp #앞쪽에 추가하므로 재정립
        return True
    
    def remove(self,key):
        hash=self.hash_value(key)
        target=self.Hash_table[hash]
        back_tracking=None
        
        while target is not None:
            if target.key==key:
                if back_tracking==None:
                    back_tracking==self.Hash_table[hash]
                    print("삭제완료")
                    return True
                else:
                    back_tracking.next=target.next
                    print("삭제완료")
                    return True
            back_tracking=target
            target=target.next
        return False #동일KEY값 검색실패
    
    def dump(self):
        for i in range(self.capacity):
            target=self.Hash_table[i]
            print(f"{i} index dump",end="")
            while target is not None:
                print("-> {} {}".format(target.key,target.value),end="")
                target=target.next
            print()
            
    def search(self,key):
        hash=self.hash_value(key)
        target=self.Hash_table[hash]
        count=0
        while target is not None:
            if target.key==key:
                print(f"{count} 번쨰 index 해당 key {target.key} vlaue {target.value}")
                return target.value
            target=target.next
            
        return False    
    
if __name__=="__main__":
    H1=ChainedHash(5)
    H1.add(15,"kello")
    H1.add(25,"HELLO")
    H1.add(35,"TEST")
    H1.remove(25)
    H1.add(25,"HELLO")
    H1.dump()
    H1.search(25)
    print()  
        
                
        

            
    

        