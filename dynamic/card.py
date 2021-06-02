# 카드 구매하기 (11052번)

if __name__ == '__main__':
    n = int(input())
    items = [0] + list(map(int, input().split()))
    d = [0] * (n + 1) # 헷갈리지 않게 0으로 초기화
    d[1] = items[1]

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if d[i] <= d[i - j] + items[j]:
                d[i] = d[i - j] + items[j]

    print(d[n])