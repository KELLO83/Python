from __future__ import annotations
from typing import Any,Type
from enum import Enum
import hashlib

class Status(Enum):
    """
    열겨형으로 OCCUPIED EMPTY DELETED를 정의한다
    """
    OCCUPIED=0
    EMPTY=1
    DELETED=2
    
class bucket:  
    #속성으로 key vlaue status를 가진다
    def __init__(self,key=None,value=None,stats=Status.EMPTY) -> None:
        self.key=key
        self.value=value
        self.stats=stats
        
    def set(self,key,value,stats):
        self.key=key
        self.value=value
        self.stats=stats
    
    def set_status(self,stats):
        self.stats=stats
    
class OpendHash:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.table=[bucket() for _ in range(self.capacity)] #opendhash 클래스를 capacity용량만큼  buket 클래스의 table을만든다
        
    def hash_value(self,key):
        if isinstance(key,int):
            return key%self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)
        
    def rehash_value(self,key): #한칸씩 이동한다
        return(self.hash_value(key) + 1) % self.capacity # 0번지에서 3번지로이동하네...????

    
    def search_node(self,key):
        hash=self.hash_value(key) #사용자가 입력한 키값을 hash함수를 이용하여 해시값을 hash에 저장한다
        target_node=self.table[hash]  #self.table[해시값]을 타겟으로 잡는다
        
        for i in range(self.capacity): #OpendHash 용량만큼 for문을 돌린다
            if target_node.stats==Status.EMPTY:
                break #해당 키값을 가진 노드가 없습니다 종료
            elif target_node.stats==Status.OCCUPIED and target_node.key==key:
                return target_node #해당 키값을 가진 노드를 리턴합니다
            hash=self.rehash_value(hash) # 해시칸수를 앞으로떙깁니다
            target_node=self.table[hash]
        
        return None #용량만큼 for문을 돌았지만 찾지못하였습니다
    
    def search(self,key):
        """ 키가 key인 갖는 원소를 검색하여 값을 반환합니다"""
        node_value=self.search_node(key)
        if node_value is not None:
            return node_value
        return None # node_value가 None일경우 검색실패
    
    def add(self,key,value):
        """key와 value를 받아서 노드에 추가합니다"""
        
        if self.search(key) is not None:
            return False #self.search 에서 return이None이 아닐경우 똑같은 key값을가진노드가 존재한다는것
        hash=self.hash_value(key)
        node=self.table[hash]
        for i in range(self.capacity):
            if node.stats==Status.EMPTY or node.stats==Status.DELETED:
                self.table[hash]=bucket(key,value,Status.OCCUPIED)
                return True
            hash=self.rehash_value(hash)
            node=self.table[hash] #한칸이동 
            
        return False #hash table full상태일경우 삽입이 불가하다
            
    def remove(self,key):
        """해당 key값을 가진 Node를 삭제합니다"""
        hash=self.hash_value(key)
        target_node=self.table[hash]
        for i in range(self.capacity):
            if target_node.stats==Status.OCCUPIED and target_node.key==key:
                print("해당 key값 {}을가진 {} 번쨰노드가 삭제됩니다".format(key,i))
                target_node.key=None
                target_node.stats=Status.DELETED
                target_node.value=None
                return True
            hash=self.rehash_value(hash)
            target_node=self.table[hash]
        
        return False #해당 KEY값을 가진 노드를 삭제하지못하였습니다
    
    def dump(self):
        """ 해시테이블에있는 모든원소를 출력합니다 """
        for i in range(self.capacity):
            if self.table[i].stats==Status.OCCUPIED:
                print("{}번째 노드에 value {} 가 저장 key {} 저장".format(i,self.table[i].value,self.table[i].key))
                continue
            elif self.table[i].stats==Status.EMPTY:
                print("{}번쨰 노드는 empty상태입니다".format(self.table[i]))
                continue
            elif self.table[i].stats==Status.DELETED:
                print("{} 번쨰 노드는 삭제유지상태입니다".format(i))
                continue
            
            
            
if __name__=="__main__":
    H1=OpendHash(5)
    H1.add(15,"kello")
    H1.add(25,"JELLO")
    H1.remove(25)
    H1.add(35,"KILO")
    H1.add(45,"dsban")
    H1.add(55,"FOX")
    H1.add(65,"july")
    H1.remove(25)
    H1.dump()
    print("DEBUG")
            