# 숫자 카드 게임
# 1. N * M 개의 카드를 입력받는다.
# 2. 행을 선택한다.
# 3. 선택한 행에서 가장 작은 수를 선택한다.
# 4. 가장 작은 수들 중에서 큰 값을 출력한다.

def min_max(n):
    result = 0
    min_val = 0

    for _ in range(n):
        datas = list(map(int, input().split()))

        for data in datas:
            if min_val == 0 or data < min_val:
                min_val = data

        if result < min_val:
            result = min_val
            min_val = 0

    print(result)

def best_answer():
    n, m = map(int, input().split())
    result = 0

    for _ in range(n):
        data = list(map(int, input().split()))
        min_val = min(data)
        result = max(result, min_val) # max()에는 iterable한 데이터만 넣어야 하므로 처음 진입시 비교 대상이 없으므로 result =0을 넣어준다.

    print(result)

if __name__ == '__main__':
    print("행,열 n과 m을 입력: ", end='')
    n, m = map(int, input().split())

    min_max(n)
    # best_answer()