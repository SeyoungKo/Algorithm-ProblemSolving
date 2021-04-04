# 왕실의 나이트
# 8*8 좌표 평면에서
# 1. 기사는 L자 형태 (수직으로 두칸, 수평으로 한칸) or ㄴ자 형태 (수직으로 한칸, 수평으로 두칸)로 이동한다.
# 2. 기사의 위치가 주어졌을 때 이동할 수 있는 경우의 수 ?

def move_knight(loc):
    n = 8
    x_y = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    move_case = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    count = 0

    x = int(x_y.get(loc[0]))
    y = int(loc[1])

    for mc in move_case:
        tmp_x = x + mc[0]
        tmp_y = y + mc[1]
        if tmp_x >= 1 and tmp_y >= 1 and tmp_x <= n and tmp_y <= n:
            count += 1
    print(count)

if __name__ == '__main__':
    print("location: ", end='')
    loc = str(input())

    move_knight(loc)