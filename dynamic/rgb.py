# RGB거리 (1149번)

if __name__ == '__main__':
    n = int(input())
    colors = []

    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    d = [[0] * 3 for _ in range(n)]

    for i in range(n):
        if i == 0: # 첫번째 행
            d[i][0] = nums[i][0]
            d[i][1] = nums[i][1]
            d[i][2] = nums[i][2]
            continue
        # 행의 모든 경우의 수
        d[i][0] = nums[i][0] + min(d[i-1][1], d[i-1][2]) # R
        d[i][1] = nums[i][1] + min(d[i-1][0], d[i-1][2]) # G
        d[i][2] = nums[i][2] + min(d[i-1][1], d[i-1][0]) # B

    min_val = min(d[n-1][0], d[n-1][1])
    min_val = min(min_val, d[n-1][2])
    print(min_val)