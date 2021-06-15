# 바이러스 (2606번)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    cnt = 0
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = list(map(int, input().split(' ')))
        graph[v1].append(v2) # 양방향 간선
        graph[v2].append(v1) # 양방향 간선

    visited = [False] * (n+1)

    # dfs(graph, 1, visited)
    print(graph)
