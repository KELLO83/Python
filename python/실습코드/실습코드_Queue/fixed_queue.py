# 고정 길이 큐 클래스 FixedQueue 구현하기
# Do it! 실습 4-3 [A]
from typing import Any

class FixedQueue:

    class Empty(Exception): #Queue가 empty상태일떄 Exception 예외처리를 print한다
        print(Exception)
        """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
        pass

    class Full(Exception): #full상태일떄 Exceiption 에외처리를 print한다
        print(Exception)
        """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int) -> None : # queue 속성으로는 queue의 원소의 갯수 enqueue를 하는 위치인 front
        # dequeu를 하는 rear 그리고 queue의 용량을 사용자로부터 입력받은 capaicty만큼 queue테이블의 크기를 정의한다
        """초기화 선언"""
        self.no = 0     # 현재 데이터 개수
        self.front = 0  # 맨앞 원소 커서
        self.rear = 0   # 맨끝 원소  커서
        self.capacity = capacity      # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체

    def __len__(self) -> int: # __len__ magic method 를 통하여 queue에있는 elemt의 갯수를 return한다
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool: # queue에있는  원소의 갯수를 확인하여 0보다 작거나 같을때를 확인하여 queue가 empty 상태인지 확인한다
        # 이떄 self.no==0 이 아닌이유는 모종의 오류로 0보다 작아지는 음수일경우가 생길수도있으므로 self.no<=0 으로 작성한다
        """큐가 비어 있는지 판단"""
        return self.no <= 0

    def is_full(self) -> bool: #queue에있는 원소의 갯수를 확인하여 queue의 capaicty보다 크거나 같은경우 queue의 용량이 가득찼음을 확인할수있다
        # 원소의갯수가 capaicty보다 커질경우 true를 return한다
        """큐가 가득 찼는지 판단"""
        return self.no >= self.capacity

# Do it! 실습 4-3 [B]
    def enque(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full  # 큐가 가득 찬 경우 예외처리를 발생
        self.que[self.rear] = x # enqueue의 위치는 rear위치에서 삽입한다 
        #  self.que[self.rear] 가 queue에 index위치이다 사용자에게 받은 x를 삽입한다
        self.rear += 1 #이후 enqueu를 진행하면서 rear의 위치를 한개증가시키면서 front는 dequeue를 진행하지않았기에 조정하지않는다
        self.no += 1 # 원소를 한개 삽입을 진행함으로써 원소의 갯수를 한개 증가시킨다
        if self.rear == self.capacity: #서클큐로써 원소를삽입후 rear의 값을증가시킨다 이때 queue 의 capacity보다 커질경우 rear idx번호를 0으로 조정함으로써 circle queue를 구현한다            self.rear = 0
            self.rear=0 #rear값 초기화
# Do it! 실습 4-3 [C]
    def deque(self) -> Any: 
        """데이터를 디큐합니다"""
        if self.is_empty(): #dequeue는 queueu table에서 원소를 한개 꺼냄으로써 원소의 갯수가 최소 한개이상 있어야한다 확인
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
        x = self.que[self.front] #dequeue 는 front방향에서진행한다 self.queue[self.front] 를통해 해당 value를 x에저장한다
        self.front += 1 #dequeue를 함으로써 front위치를 그다음 idx번호로 이동함한다
        self.no -= 1 #원소를 하나꺼냄으로써 원소으 갯수를 한개줄인다
        if self.front == self.capacity: #circle queue로써 front가 용량이랑 같아질경우  front위치를 0으로 재조정한다
            self.front = 0 #위치조정 
        return x

# Do it! 실습 4-3 [D]
    def peek(self) -> Any:
        """데이터를 피크합니다(맨 앞 데이터를 들여다 봄)"""
        if self.is_empty(): #원소의 갯수가 최소 1개여야 peek가 가능하다
            raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
        return self.que[self.front] # queue는 FIFO 구조로써  enqueue의 마지막부분인 front방향의 데이타를 본다

    def find(self, value: Any) -> Any: 
        """큐에서 value를 찾아 인덱스를 반환하고 없으면 -1을 반환합니다"""
        for i in range(self.no): #for문의 진행범위 queue의 원소의 갯수만큼 진행한다
            idx = (i + self.front) % self.capacity #이떄 서클큐로써 인덱스번호를 %self.capacity으로 front시작위치를 찾는다
            if self.que[idx] == value:  # 검색 성공  
                return idx #해당 원소의 저장되어있는 queue의 idx번호를 return합니다
        return -1  # 검색 실패 false

    def count(self, value: Any) -> bool:
        """큐에 포함되어 있는 value의 개수를 반환합니다"""
        c = 0 #사용자가 찾고자하는 원소의 갯수를 c라는변수를통해 count합니다
        for i in range(self.no):  # 큐 데이터를 선형 검색  range(self.no) 를통해 queue에있는 원소의 elem 갯수만큼 for문으 순회합니다
            idx = (i + self.front) % self.capacity #서클큐로써 인덱스번호 찾아가기 #73 행의 설명과 동일함
            if self.que[idx] == value:  # 검색 성공 
                c += 1  # 들어있음 #사용자가 찾고자하는 원소의 갯수를 하나 증가합니다
        return c #for문을통해 사용자가 찾고자하는 value값이 queue에 얼만큼들어있는지 return합니다

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 포함되어 있는지 판단합니다"""
        return self.count(value)

    def clear(self) -> None:
        """큐의 모든 데이터를 비웁니다"""
        self.no = self.front = self.rear = 0 #원소의 갯수0 front ,rear를 0으로 초기화함으로써 초기상태의 queue로 만듭니다

    def dump(self) -> None:
        """모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다"""
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            print('큐가 비어 있습니다.') #큐가 비어있다면 dump할 원소가 없으므로 예외처리를 발생합니다
        else:
            for i in range(self.no): #queue에있는 원소의 갯수만큼 for문을 순회합니다
                print(self.que[(i + self.front) % self.capacity], end=' ') # 73행설명과 동일 그 idx에 저장되었닌 value를 print합니다
            print() #줄바꿈
                
