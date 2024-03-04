# [Do it! 실습 5-9] 8퀸 문제 알고리즘 구현하기

pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(y: int) -> None: 
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if(     not flag_a[j]            # j행에 퀸이 배치 되지 않았다면
            and not flag_b[y + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[y - j + 7]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[y] = j  # 퀸을 j행에 배치
            if y == 7:  # 모든 열에 퀸을 배치하는 것을 완료
                put() 
            else:
                flag_a[j] = flag_b[y + j] = flag_c[y - j + 7] = True
                set(y + 1)  # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[y + j] = flag_c[y - j + 7] = False # 룩 3*3 (0,1,2) (0,2,1) 메이플 루디브리엄 커닝시 
#0,0,0 -> 0,0,1 ->0,0,2-> 0,1,0 ->0,2,0->1,0,0->1,0,1->1,0,2->1,1,0 ->1,2,0->1,0,1->1,0,2.... 0,1,2 0은 아직픽스드 1 ,2 가바뀌면서 또찾느거야 재귀안에 재귀가 2번호출 경우의수찾기 수 하나씩증가시키면서if문을통해서 검사하는거지

def test():
    print("hello")
    test()#재귀함수
    print("종료") 
'''
hello
hello ->처음불러진test안에 test헬로
종료 ->처음불러진test안에 test종료
종료->처음불러진 test
'''
set(0)  # 0열에 퀸을 배치
