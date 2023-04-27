# 정수 삼각형 (1932번)

if __name__ == '__main__':
    # n = int(input())
    # arrs = []
    # for _ in range(n):
    #     inputs = list(map(int, input().split()))
    #     arrs.append(inputs)

    # k = 2
    # for i in range(1, n):
    #     for j in range(k): # 두번째 줄부터
    #         if j == 0:
    #             arrs[i][j] = arrs[i][j] + arrs[i - 1][j]
    #         elif i == j: # 각 줄의 맨 끝에 위치한 원소는 바로 자기 위 숫자를 더한다.
    #             arrs[i][j] = arrs[i][j] + arrs[i - 1][j - 1]
    #         else: # 나머지 원소는 왼쪽 위 / 오른 쪽 위 중 큰 값을 더한다.
    #             arrs[i][j] = arrs[i][j] + max(arrs[i - 1][j - 1], arrs[i - 1][j])
    #     k += 1
    # print(max(arrs[n - 1]))

    n = int(input())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    k = 2
    for i in range(1, n):
        for j in range(k):
            if j == 0:
                t[i][j] = t[i][j] + t[i - 1][j]
            elif i == j:
                t[i][j] = t[i][j] + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
        k += 1
    print(max(t[n - 1]))


