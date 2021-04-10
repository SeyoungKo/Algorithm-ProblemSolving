# 떡볶이 떡 만들기

def maker(inputs, m, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    share = 0

    for item in inputs:
        if item > mid:
            share += item - mid

    if share == m:
        return mid

    elif share < m:
        return maker(inputs, m, start, mid-1)

    elif share > m:
        return maker(inputs, m, mid + 1, end)


if __name__ == '__main__':
    print("N, M: ", end='')
    n, m = map(int, input().split())
    inputs = list(map(int, input().split()))
    sorted(inputs)

    print(maker(inputs, m, 0, max(inputs)))