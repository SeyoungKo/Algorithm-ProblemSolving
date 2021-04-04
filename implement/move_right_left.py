# 상하좌우
# N을 입력받는다.
# 1. N * N 크기의 정사각형 공간에서 사용자가 입력한 움직임 횟수만 상하좌우 이동한다.
# 2. 1*1 좌표에서 좌, 상으로 이동하려고 하면 x
# 3. n*n 좌표에서 하, 우로 이동하려고 하면 x
# 4. 최종적으로 모험가가 도착하는 좌표를 출력한다.
# L, R, U, D

def move(route, n):
    move_types = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1] # move x (move types와 인덱스 대응)
    dy = [-1, 1, 0, 0] # move y (move types와 인덱스 대응)
    x, y = 1, 1 #현재 위치
    tmp_x, tmp_y = 0, 0

    for r in route:
        for idx, move_type in enumerate(move_types):
            if r == move_type:
                tmp_x = x + dx[idx]
                tmp_y = y + dy[idx]
        if tmp_x < 1 or tmp_y <1 or n < tmp_x or n < tmp_y:
            continue
        x, y = tmp_x, tmp_y
    print("({}, {})".format(x,y))

if __name__ == '__main__':
    print("만들려는 정사각형 크기를 입력 ! :", end='')
    n = int(input())

    move_to = list(map(str, input().split()))
    move(move_to, n)