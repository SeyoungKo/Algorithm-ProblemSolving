# 파이썬으로 큐 구현하기
from collections import deque

def queue():
    q = deque()

    q.append(8)
    q.append(7)
    q.append(6)
    q.append(5)
    q.append(4)
    q.popleft()
    q.append(2)
    q.popleft()

    print(q)
    print(type(q))
    q.reverse() # deque 라이브러리는 마스킹으로 순서를 바꿔서 출력할 수 없다. reverse 사용해야 함
    print(q)


if __name__ == '__main__':
    queue()