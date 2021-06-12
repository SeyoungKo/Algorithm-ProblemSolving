# dfs와 bfs (1260번)
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = False

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

if __name__ == '__main__':
    info = list(map(int, input().split(' ')))
    n = info[0]
    m = info[1]
    start = info[2]

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = list(map(int, input().split(' ')))
        graph[v1].append(v2) # 양방향 간선
        graph[v2].append(v1) # 양방향 간선

    # print(graph)
    visited = [False] * (n + 1)

    dfs(graph, start, visited)
    print()
    bfs(graph, start, visited)
