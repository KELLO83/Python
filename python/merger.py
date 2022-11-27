# [Do it! 실습 6-15] 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:


    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right: 
            center = (left + right) // 2  #중간 반띵

            _merge_sort(a, left, center)  #분할정복
            _merge_sort(a, center + 1, right) 

            p = j = 0
            i = k = left

            while i <= center:
                 buff[p] = a[i]  #작업용배열에 기존배열의 절반만 일단 넣는다
                 p += 1  
                 i += 1 

            while i <= right and j < p: # i는 원본배열의 뒷부분 j는 버퍼의 앞부분 p는  버퍼의 끝부분
                 if buff[j] <= a[i]: # 뒷부분의 배열의 값이 크다면 현재 오름차순이고 작업용 배열의 buff[j] 가 a[i]보다 값이작은것
                     a[k] = buff[j]  # 원본배열삽입할자리에 작업용배열의값을 삽입한다
                     j += 1  # 작업용배열의 위치포인터 증가
                 else: 
                     a[k] = a[i] # 뒷부분의 배열의값이 작은것 작업용배열보다 그러므로 원본배열의 삽입할자리에 뒷부분의 배열의 데이터값을 삽입한다 
                     i += 1  # 뒷부분배열의 위치포인터 증가
                 k += 1

            while j < p: 
                a[k] = buff[j]  #작업용배열의 남은 데이터들을 원본배열의 뒤쪽에 삽입한다
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           
    _merge_sort(a, 0, n - 1)    
    del buff                   

if __name__ == '__main__':
    print('병합 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')