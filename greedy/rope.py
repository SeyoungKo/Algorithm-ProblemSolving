# 로프 (2217번)

if __name__ == '__main__':
    n = int(input())
    m = [int(input()) for _ in range(n)]

    max_m = min(m) * n
    res = max_m
    m.sort(reverse=True)

    for i in range(1, len(m)+1):
        val = i * m[i-1]
        print(f'val:{val}, res:{res}')
        if res < val:
            res = val

    print(res)