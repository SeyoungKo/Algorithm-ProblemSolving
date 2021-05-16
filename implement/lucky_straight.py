# 럭키 스트레이트
# 점수 N이 주어질 때 반으로 나눠 왼쪽과 오른쪽 값의 합이 동일하면 LUCKY, 아니면 READY

if __name__ == '__main__':
    print('N:', end='')
    n = input()

    half = int(len(n)/2)
    left = list(map(int, n[:half]))
    right = list(map(int, n[half:]))

    print('LUCKY' if sum(left) == sum(right) else 'READY')