# [Do it! 실습 6-15] 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:


    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right: # left right 는 idx번호이다
            center = (left + right) // 2 #Center를 기준으로 2개로쪼갠다

            _merge_sort(a, left, center)  # 재귀호출로 원본배열의 왼쪽부분을 정렬시킨다
            _merge_sort(a, center + 1, right) # 재귀호출로 원본배열의 오른쪽부분을 정렬시킨다

            p = j = 0
            i = k = left

            while i <= center: # 원본배열의 앞부분을 작업용buffer에 붙혀넣기..
                 buff[p] = a[i]
                 p += 1 
                 i += 1

            while i <= right and j < p: #배열뒷부분과 작업용버퍼를 비교하여 원본배열애 정렬시킨다
                 if buff[j] <= a[i]: #작업용배열의 원소가 작다면 원본배열의 뒷부분의 원소가 크다는것 작업용배열의 원소보다
                     a[k] = buff[j] #그러므로 원본배열에 버퍼의 원소를 삽입한다
                     j += 1 #작업용배열에서 삽입했으므로 작업용배열의 칸수를 하나 증가시킨다..
                 else: #원본배열의 뒷부분의 원소가 크다는것이다..
                     a[k] = a[i] # 그러므로 원본배열에다가 원본배열의 뒷부분의 원소를 삽입한다
                     i += 1 # 원본배열의 뒷부분에서 삽입한거이므로 원본배열의 뒷부분의 idx를 증가시킨다
                 k += 1

            while j < p: #작업용배열에서 남은 원소들을 원본배열의 뒷부분에 붙힌다..
                a[k] = buff[j] 
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