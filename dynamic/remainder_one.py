# 1로 만들기
# 정수 x가 주어질 때 사용할 수 있는 연산은 다음과 같이 4가지이다.
# 1. x가 5로 나누어떨어지면 5로 나눈다.
# 2. x가 3으로 나누어떨어지면 3으로 나눈다.
# 3. x가 2로 나누어떨어지면 2로 나눈다.
# 4. x에서 1을 뺀다.
# 최소한의 연산 사용개수로 1을 만들 때 연산횟수는?

def remainder(n):
    d = [0] * 100000

    for i in range(2, n+1):
        # 현재 수에서 1을 빼는 경우
        d[i] = d[i-1] +1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] +1) # 반복 호출될 때마다 +1씩 증가된다.
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] +1) # 반복 호출될 때마다 +1씩 증가된다.
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] +1) # 반복 호출될 때마다 +1씩 증가된다.

    print(d[n])


if __name__ == '__main__':
    print("num:", end='')
    n = int(input())
    remainder(n)