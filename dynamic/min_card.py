# 카드 구매하기2 (16194)

if __name__ == '__main__':
    n = int(input())
    items = [0] + list(map(int, input().split()))
    d = [False] * (n + 1) # 0으로 초기화하지 않고 min을 사용하기 위해 false로 초기화

    d[1] = items[1] # n=1은 경우의 수가 한가지
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if d[i] is False:
                d[i] = d[i - j] + items[j]
            else:
                d[i] = min(d[i], d[i - j] + items[j])
    print(d[n])

