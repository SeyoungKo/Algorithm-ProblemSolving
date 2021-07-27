# bfs (너비우선탐색)
from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    visited[start] = True
    queue.append(start)

    print("BFS search node :", end='')
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] is False:
                visited[i] = True
                queue.append(i)

def queue_bfs(graph, start):
    queue_, visited = [], []
    queue_.append(start)

    while queue_:
        node = queue_.pop(0)
        if node not in visited:
            visited.append(node)
            queue_.extend(graph[node])

    return visited

if __name__ == '__main__':
    # graph[i]의 노드들 = 너비우선탐색으로 탐색한 노드들
    # graph[i]의 노드들을 방문한 노드인지 확인하면서
    # 방문하지 않은 노드는 queue에 저장한다
    # queue에 저장되었던 front 노드를 호출 (graph[i][0] 노드)
    # graph[front]의 노드들을 탐색
    # ... 반복한다

    # 너비우선탐색이라서 graph[i]의 노드들을 (방문한 노드 제외하고) 모두 queue에 넣고 순차적으로 popleft한다
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    graph_alpha = dict()

    graph_alpha['A'] = ['B', 'C']
    graph_alpha['B'] = ['A', 'D']
    graph_alpha['C'] = ['A', 'G', 'H', 'I']
    graph_alpha['D'] = ['B', 'E', 'F']
    graph_alpha['E'] = ['D']
    graph_alpha['F'] = ['D']
    graph_alpha['G'] = ['C']
    graph_alpha['H'] = ['C']
    graph_alpha['I'] = ['C', 'J']
    graph_alpha['J'] = ['I']

    visited = [False] * 9

    bfs(graph, 1, visited)
    print('')
    print(queue_bfs(graph_alpha, 'A'))