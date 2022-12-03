import random
from typing import *

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center: # 임시배열에다가 a배열의 앞부분을 복사한다
                 buff[p] = a[i]
                 p += 1
                 i += 1
            # 완료후 i,p는 배열의 중간지점까지왔다
            
            while i <= right and j < p: # a[i]의 후반부가 배열의끝지점올떄까지 이면서 j=0부터 임시배열 buff[j]의 j포인터가 buff의 끝지점올떄까지
                 if buff[j] <= a[i]: # 임시배열의 원소의크기가 작습니다
                     a[k] = buff[j] # k=0부터 대입한다
                     j += 1
                 else: # 원본배열의 후반부가 작습니다
                     a[k] = a[i]
                     i += 1
                 k += 1

            while j < p: # 임시배열의 남은부분을 넣습니다
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬
    del buff                    # 작업용 배열을 소멸


if __name__ =="__mmain__":
    data=[random.randrange(20) for _ in range(10)]
    print("정렬전data===>",data)
    merge_sort(data)   