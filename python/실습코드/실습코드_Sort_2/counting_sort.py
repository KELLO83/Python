# [Do it! 실습 6-17] 도수 정렬 알고리즘 구현하기

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)       # 배열의 길이 
    f = [0] * (max + 1)  # 누적도수 분포표 카운팅 배열
    b = [0] * n         #  작업용 배열

    for i in range(n):       
        f[a[i]] += 1 # a[i]의 원소값을 f[원소값] idx 번호에서 하나증가시킨다               
        
    for i in range(1, max + 1):     
        f[i] += f[i - 1]  # 누적도수 분포포 구성... 앞의idx의 value들을 합산해간다       
       
    for i in range(n - 1, -1, -1):# 스캔방향 top -> bottom
        f[a[i]] -= 1 
        b[f[a[i]]] = a[i]  #작업용배열에다가 원본배열의 원소를 삽입한다
         
    for i in range(n):              
        a[i] = b[i]                    

def counting_sort(a: MutableSequence) -> None:
    """도수 정렬"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('도수 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):  # 양수만 입력받음
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break

    counting_sort(x)  # 배열 x를 도수 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')