# A->B (16953번)
from collections import deque

if __name__ == '__main__':
    start, end = map(int, input().split())
    count = 1
    q = deque([(start, 1)])

    while q:
        start, cnt = q.popleft()
        if start == end:
            count = cnt
            break

        if start * 2 <= end:
            q.append((start * 2, cnt + 1))

        if int(str(start)+'1') <= end:
            q.append((int(str(start)+'1'), cnt + 1))

    if start != end:
        count = -1

    print(count)