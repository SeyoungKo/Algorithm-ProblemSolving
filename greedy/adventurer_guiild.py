# 모험가 길드
# N명의 모험가 정보가 주어질 때 최소 자신의 공포도 수치 이상의 사람으로 구성된 그룹에 포함되어야 함
# 여행을 떠날 수 있는 그룹의 최댓값은?

if __name__ == '__main__':
    print('N: ', end='')
    n = int(input())

    print('fear: ', end='')
    fear = list(map(int, input().split()))
    fear.sort()
    print(fear)

    result = 0
    count = 0

    for person in fear:
        count += 1
        if count >= person:
            result += 1
            count = 0

    print(result)