

#소수란 2보다 큰자연수에서 1과 자기자신을 제외한 자연수로 나누어떨어지지않는다
#에라토스체네스의 체 
from typing import Sequence
import collections
import copy
# def ck(start,Max_data):
#     for i in range(start+1,Max_data):
#         if n%i!=0:
#             return True
#         else:
#             return False

# def get_prime(n:Sequence) -> int:
#     count=0
#     while n:
#         out_data=n.pop();
#         if out_data<=1:
#             continue
#         else:
#             for i in range(2,out_data):
#                 if out_data%i==0:
#                     break
#             else:
#                 count+=1    
                
#     return count

# https://this-programmer.tistory.com/409
"""
logic 구상
1. list에서 첫번째원소의 데이터를 끄집어낸다
2. 첫번째원소를 제외한 첫번째원소의 배수들을 삭제한다 (단 1이아닌..)
3. 삭제된원소들에서 아닌 두번쨰원소를 택한후 두번째원소를 남기고 두번째원소의 배수들을 삭제한다
    세부구성.
    1.inspect검사한숫자는 더이상 기존배열에서 순회할때 검사에들어가면언된다..
    2. 기존배열에서 삭제를 진행하면 len(arr) 사이즈가 달라지므로 while문을 사용해야한다 idx point를 설정하여 하나씩증가시킨다..
    3. 
4. 언제까지..? list에서 모두 순회를 마칠때까지..
"""

idx=0
idx_count=0
def Eratosthenes(n:Sequence)->int: 
    global idx
    global idx_count
    n.sort()
    print(n)
    delelt_list=list()
    copy_list=copy.deepcopy(n)
    n=collections.deque(n) # n [1,3,5,6,9] 라면 소수는 5 한개  
    while n: 
        inspect=n[idx_count] # 3부터꺼낸다
        if inspect<=1:
            copy_list.remove(inspect)
            idx_count+=1
            continue
        else:
            for i in range(idx,len(copy_list)):
                if copy_list[i]==inspect:
                    continue
                else:
                    if copy_list[i] % inspect==0:
                        delelt_list.append(copy_list[i])
        print(copy_list)
        print(delelt_list)
        while delelt_list:
            target=delelt_list.pop()
            copy_list.remove(target)
        print(copy_list)
        idx_count+=1
        
        
if __name__=="__main__":
    n=int(input())     
    user=list(map(int,input().split()))
    user=user[:n]
    Eratosthenes(user)