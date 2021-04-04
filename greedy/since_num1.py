# 1이 될 때까지
# 1. 1이될 때까지 N을 1로 빼거나 k로 나눈다.
# 2. 나누기는 나머지가 0일때만 가능하다
# 3. 최소 수행 횟수를 구한다.

def get_num(n,k):
    count = 0
    print(type(n))
    while n >= k:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        count += 1

    # 나머지 큰 수 처리 (1로 만들기)
    if n != 1:
        while n > 1:
            n -= 1
            count += 1

    print("최소 {}회 수행, result : {}".format(count, n))

if __name__ == '__main__':
    print("n, k: ", end='')
    n, k = map(int, input().split())
    get_num(n,k)
