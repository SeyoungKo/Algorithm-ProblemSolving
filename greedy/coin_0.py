# 동전 0 (11047번)
# N개의 동전 종류와 K가 주어질 때 K가 되는 최소의 동전 개수
def best_answer(coins, k):
    count = 0

    for coin in coins:
        if coin > k:
            continue
        if coin <= k:
            share = k // coin
            k -= coin * share
            count += share

    return count

def solve(coins, k):
    count = 0

    for coin in coins:
        if coin > k:
            continue
        while k >= coin:
            k -= coin
            count += 1

    return count

if __name__ == '__main__':
    print('N, K: ', end='')
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    coins.sort(reverse=True)

    print(best_answer(coins, k))