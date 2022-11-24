# [Do it! 실습 6-10] 퀵 정렬 알고리즘 구현

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """
    퀵소트 
    1. 기준점을 기준으로 왼쪽에는 작은원소 오른쪽에는 기준보다 큰원소를 모은다
    2. 작은원소들을 모은곳에서 또 기준점을 정한후 기준점을 기준으로 작은 큰원소를 분할시킨다
    3. 언제까지..? left=pr right=pl 일때까지..
    """
    pl = left                   
    pr = right                 
    x = a[(left + right) // 2]  # 기준점 left right 중간
    # pl pr x 는 전부 idx이다 원소값이아니다....

    while pl <= pr:    # 서로 엇갈리지않는동안 즉 pr값이 더큰동안..
        while a[pl] < x: pl += 1 # 기준점으로 pl은 원소들이 작아야한다 기준보다 커서가 멈추는지점은 기준점보다 큰곳idx
        while a[pr] > x: pr -= 1 #기준점을 기준으로 pr은 원소들이 커야한다 멈추는곳은 기준점보다 원소가 작은지점...
        if pl <= pr: # pl pr은 원소value가아닌 idx값이다 착오금지...
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    # left right pr pl 은 전부 idx위치이다 원소값이아니다..
    # 즉 left==pr 이라면 원소가 1개여서 정렬불필요...
    if left < pr: qsort(a, left, pr) # left pr 은 위치값이다
    if pl < right: qsort(a, pl, right)
    """
    1.기준이되는 데이터인 pivot을 하나 선택한다
    2. pivot보다 작은데이터와 pivot보다 큰 데이터로 구분한다
    """
    

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')