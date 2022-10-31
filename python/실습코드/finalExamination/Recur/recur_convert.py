#arr의 합을구한다 단 recur을 이용하여
import random
def call(arr,n):
    if n<=0: #n이 0보다 작다는것은 배열이 한칸만 남아있다
        return arr[0] #배열한칸의 값을 반환한다
    else: #n이 한칸이 아니라면? 적어도 두칸이상을 가지고있다
        return call(arr,n-1)+arr[n]  #리턴값에다가 끝배열의 원소의값을 더한것을 반환한다
    
"""
그렇다면 3개는?
[1,2,3]
call(arr,3) -> return 1+2 + 3
call(arr,2) -> retunr  1  + 2
call(arr,1) ->return 1
"""
"""
그렇다면 5개는?
              ==>최종 24가 반환된다
[10,5,4,2,3] return 21 + 3  return 21 은 call(arr,4)에서부터 비롯됨
call(arr,4)-> return 19 + 2  retunr 19는 call(arr,3)에서부터 비롯됨
call(arr,3)-> return 15 + 4  retunr15는 call(arr,2)에서부터 비롯됨
call(arr,2)-> return 10 + 5  단 이때 return10은 call(arr,1)에서부터 비롯됨
call(arr,1) -> return 10 


"""


arr=[random.randint(0,255) for _ in range(random.randint(10,20))] 
print(arr)
print(call(arr,len(arr)-1)) #시작 인수 배열 arr 인덱스번호=> 배열의 끝번호를 준다