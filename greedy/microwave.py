# 전자레인지 (10162번)
# A, B, C 3개의 버튼을 눌러 합이 T가 되도록하는 최소 횟수 구하기

if __name__ == '__main__':
    time = int(input())
    microwave = [300, 60, 10]
    res = [0, 0, 0]

    for i, mw in enumerate(microwave):
        if time < mw:
            continue
        if mw <= time:
            share = time // mw
            time -= mw * share
            res[i] += share

    for r in res:
        if time != 0:
            print(-1)
            break
        print(r, end=' ')


