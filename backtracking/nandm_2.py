from itertools import combinations


if __name __ ==  '__main__':
    N, M = map(int, input().split())
    numList = [i for i in range(1, N+1)]
    # [1, 2, 3, 4]

    for seq in combinations(numList, M):
        print(*seq)