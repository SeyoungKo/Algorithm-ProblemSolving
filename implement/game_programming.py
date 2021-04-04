# 게임 개발
# 1. N(세로), M(가로)를 입력받는다.

# 움직임 조건에 맞춰 이동시킨 후 캐릭터가 방문한 칸 수를 출력한다.
# 조건 1. 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 반복한다.
# 조건 2. 바로 왼쪽에 가보지 않은 칸이라면 왼쪽방향으로 회전하고 왼쪽으로 한칸 간다
# 조건 3. 바로 왼쪽에 가보지 않은 칸이 없으면 왼쪽으로 회전만 수행하고 1로 돌아간다
# 조건 4. 네 방향 모두 가본 칸이거나 바다인 칸이면 방향을 유지한 채로 한칸 뒤로 가고 1로 돌아간다.
#        뒤쪽 방향이 바다라 뒤로 갈 수 없으면 움직임을 멈춘다.

def move_character(n, m, a, b, d):
    arr = []
    for _ in range(n):
        # n x m 만큼 맵 조건 생성
        arr.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]  # 북, 동, 남, 서
    dy = [-1, 0, 1, 0]
    visit = [[0] * m for _ in range(n)]  # 방문 여부 초기화 (2차원 리스트)
    count = 0
    turn_time = 0

    # 시작

    # 왼쪽으로 회전

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우

    # 네 방향 모두 갈 수 없는 경우

    # 뒤가 바다로 막혀있는 경우

def turn_left(d):
    direction = d
    direction -= 1
    if direction == -1:  # 현재 위치 -1 = 반시계방향으로 이동한
        direction = 3

    return direction


if __name__ == '__main__':
    print("N, M: ", end='')
    n, m = map(int, input().split())

    print("현재 캐릭터가 있는 좌표, 방향입력 : ", end='')
    a, b, d = map(int, input().split())  # a<=n , b<=m, direction<=3 (0포함)

    move_character(n, m, a, b, d)
