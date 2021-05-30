# 1, 2, 3 더하기 (9095번)

dp = {1: 1, 2: 2, 3: 4}

def rec(n):
    if n not in dp:
        dp[n] = rec(n-1) + rec(n-2) + rec(n-3)
    return dp[n]

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        m = int(input())
        print(rec(m))
