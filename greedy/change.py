# 거스름돈 (5585번)

if __name__ == '__main__':
    n = int(input())
    money = [500, 100, 50, 10, 5, 1]
    money.sort(reverse=True)
    count = 0
    n = 1000 - n

    for m in money:
        if m > n:
            continue
        if m <= n:
            share = n // m
            n -= m * share
            count += share

    print(count)
