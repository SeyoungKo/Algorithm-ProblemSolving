# 더하기 사이클(1110번)
if __name__ == '__main__':
    n = int(input())
    count = 0
    num = n

    while True:
        first = n // 10
        second = n % 10
        sum_ = first + second
        count += 1

        n = int(str(n % 10) + str(sum_ % 10))
        if num == n:
            break
    print(count)