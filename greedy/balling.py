# 볼링공 고르기
# 무게에 따라 여러개의 볼링공이 있을 때 경우의 수를 구한다.
# A가 특정 무게의 공을 선택할 때 B는 A가 선택한 공의 무게보다 큰 공을 선택할 때 경우의 수는?

def best_answer(n, m, data):
    # 1부터 10까지 무게를 담는 리스트
    array = [0] * 11

    for x in data:
        # 각 무게별(i) 볼링공 개수
        array[x] += 1

    result = 0
    for i in range(1, m+1):
        n -= array[i] # 무게가 i인 볼링공의 개수 제외
        result += array[i] * n # 각 볼링공 번호의 경우의 수

    print(result)


def ball_case(ball):
    count = 0

    for i in range(0, len(ball)):
        for j in range(i, len(ball)):
            if ball[i] == ball[j]:
                continue
            else:
                count += 1
                print(f'({i},{j})')

    print(count)

if __name__ == '__main__':
    print('N, M:', end='')
    n, m = map(int, input().split(' '))

    print('ball:', end='')
    ball = list(map(int, input().split(' ')))

    ball_case(ball)
    best_answer(n, m, ball)

