# 효율적인 화폐 구성
# n, m이 주어지면 n개 만큼 입력한 가치의 화폐들로 최소한의 횟수로 m을 만들기 위한 개수
def effective_bills(m, value):
    d = [10001] * (m + 1)

    d[0] = 0
    for i in range(n): # 단위 화폐 개수
        for j in range(value[i], m+1): # 입력 금액만큼 반복
            d[j] = min(d[j], d[j - value[i]]+1) # min(현재금액 , (현재금액 - 타겟 화폐단위)+1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])


if __name__ == '__main__':
    print("n, m:", end='')
    n, m = map(int, input().split())
    value = [int(input()) for i in range(n)]

    effective_bills(m, value)
