# [Do it! 실습 4-4] 고정 길이 큐 클래스(FixedQueue)를 사용하기

from enum import Enum # enum class를 import하여 열거형 class를 사용합니다
from fixed_queue import FixedQueue

"""
class Menu(Enum):
    '인큐'=1
    '디큐'=2
    '피크'=3
    '검색'=4
    '덤프'=5
    '종료'=6
    
"""
Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료']) #위의 주석과 동일한 작동

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu] # Menu를 dict형태로 받아서 m.value와 m.anme {이름:키} 값형태로 전달
    while True:
        print(*s, sep='   ', end='') #*s(가변인수) 를 출력할때마 seperate작동 자동 띄워쓰기 end='' 줄바꿈 없음
        n = int(input(': ')) #n= 사용자로부터 입력한 숫자를 저장한다
        if 1 <= n <= len(Menu): #menu의 key값범위안에서 사용자가 숫자를 입력할시 실행
            return Menu(n) #Menu(사용자 입력정수) retunr한다

q = FixedQueue(64)  # 최대 64개를 인큐할 수 있는 큐 생성(고정 길이)

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}') # queue의 현재 길이와 전체 queue의길이를 print한다
    menu = select_menu()   # 메뉴 선택 함수실행

    """
    Menu는 열겨형으로써 
    인큐=1
    디큐=2
    피크=3
    검색=4
    덤프=5
    종료=6
    으로 대응된다
    """
    if menu == Menu.인큐:  # 인큐 사용자가 입력한 정수가 1==Menu.인큐일때 실행
        x = int(input('인큐할 데이터를 입력하세요.: '))
        try:
            q.enque(x) #인큐실행
        except FixedQueue.Full: #만약 큐가 full상태라면예외처리 발생 
            print('큐가 가득 찼습니다.')

    elif menu == Menu.디큐:  # 디큐 사용자가 입력한 정수가 2==Menu.디큐일떄 실행
        try:
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty: #queue에서 empty상태라면 예외처리를 발생합니다
            print('큐가 비어 있습니다.')

    elif menu == Menu.피크:  # 피크 사용자가 입력한 정수가 3==Menu.피크 일때 실행
        try: #front방향의 데이터를 참조
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty: #queue에서 empty상태라면 예외처리 발생
            print('큐가 비었습니다.')

    elif menu == Menu.검색:  # 검색 사용자가 입력한 정수가 4=Menu.검색일때 실행
        x = int(input('검색할 값을 입력하세요.: ')) #사용자가에 검색할 value 를 받습니다
        if x in q: #if 문을통해  queue안에 데이타 x가 존재하는지를 확인합니다
            print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.') #검색 실패

    elif menu == Menu.덤프:  # 덤프 검색 사용자가 입력한정수가 5=Menu.덤프 일때 실행
        q.dump() #queue에있는 모든원소를 출력합니다
    else:
        break