# 게임을 만든 동준이 (2847번)

if __name__ == '__main__':
    n = int(input())
    scores = [int(input()) for _ in range(n)]

    count = 0
    max_score = scores[len(scores)-1]

    # for i in reversed(range(len(scores)-1)):
    #     if max_score <= scores[i]:
    #         count += (scores[i] - max_score + 1)
    #     max_score = scores[i]

    for i in range(n-1, 0, -1):
        print(i)
        if scores[i] <= scores[i-1]:
            count += scores[i-1] - scores[i] + 1
            scores[i-1] = scores[i] - 1

    print(count)