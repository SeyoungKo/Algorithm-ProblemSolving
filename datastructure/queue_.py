# 파이썬으로 큐 구현하기
from collections import deque
from queue import PriorityQueue

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

# 우선순위 큐
def priority_queue():
    data_queue = PriorityQueue()
    # 튜플 형식으로 우선순위를 정해준다. (숫자가 낮을수록 우선순위가 높다)
    data_queue.put((10, 'korea'))
    data_queue.put((5, 1))
    data_queue.put((15, 'china'))
    print(data_queue.get())

if __name__ == '__main__':
    queue()
    priority_queue()
