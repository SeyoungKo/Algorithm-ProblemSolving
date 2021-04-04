# 큰 수의 법칙
# 1. N : 배열의 크기 , M : 숫자가 더해지는 횟수, K : 연속 사용 가능 횟수
# 2. 연속된 큰 수 사용 k회 가능
# 3. 중복되는 수 연속 사용 가능
# 4. M회에 딱 맞춰서 수행
# 5. k회 채우고 번갈아가면서 여러번 사용 가능

def continous_num(m, k, arrs):
    sort = sorted(arrs, reverse=True)
    res = 0

    while True:
        if m == 0:
            break
        else:
            for _ in range(k):
                if m == 0:
                    break
                res += sort[0]
                print("{} + ".format(sort[0]), end='')
                m -= 1

            if m == 0:
                break
            res += sort[1]
            print("{} + ".format(sort[1]), end='')
            m -= 1
    print("= {}".format(res), end='')


def best_answer(n, m, k, arrs):
    arrs.sort()
    first = arrs[n-1]
    second = arrs[n-2]
    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            print("{} + ".format(first), end='')
            m -= 1
        if m == 0:
            break
        result += second
        print("{} + ".format(second), end='')
        m -= 1
    print("= {}".format(result), end='')

def user_in():
    print("N: ", end='')
    n = int(input())
    print("M: ", end='')
    m = int(input())
    print("K: ", end='')
    k = int(input())

    print("숫자 입력: ".format(n), end='')
    arr_nums = list(map(int, input().split()))  # 입력개수 제한 x

    continous_num(m, k, arr_nums)
    # best_answer(n, m, k, arr_nums)


if __name__ == '__main__':
    user_in()
