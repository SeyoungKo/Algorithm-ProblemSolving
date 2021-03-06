# 오르막 수 (11057번)

if __name__ == '__main__':
    n = int(input())
    d = list([[0] * 10 for _ in range(3)])

    # 1. n=1일 때
    # 0 -> (0~9) 10가지

    # 2. n=2일 때
    # 앞자리가 0이면 -> (0~9) "" 1이면 -> (1~9) "" 2이면 -> (2~9) "" 3이면 -> (3~9) ... 55가지

    # 3. n=3일 때
    # 앞자리가 0이면 -> 0 + (k~9) + (둘째자리에서 결정된 수 ~ 9) ... -> 220가지

    # -> 가운데 오는 숫자에 따라 그 숫자보다 큰 경우의 수를 모두 더한다.
    # N번째 d에서 k의 경우의 수는 n-1번째 d의 k~9까지의 합과 같아진다.

    # i = 경우의 수를 결정하는 값
    for i in range(10):
        d[1][i] = 1 # n=1
        d[2][i] = 10 - i # n=2 i 값에 따라 경우의 수가 줄어든다.

    for j in range(3, n + 1): # n=3 이상
        tmp = [0] * 10
        for k in range(10):
            if k == 9:
                tmp[k] = 1 # 9는 경우의 수가 한개
            else:
                tmp[k] = sum(d[j-1][k:]) % 10007 # n-1번째 d의 k~9까지 경우의 수 합계
        d.append(tmp) #d[n]으로 결과를 보여줄 수 있게

    print(sum(d[n]) % 10007)


