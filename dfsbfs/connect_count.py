# 연결요소의 개수 (11724번)
import sys
sys.setrecursionlimit(10000) # 재귀제한 풀기

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    cnt = 0

    for _ in range(m):
        v1, v2 = list(map(int, input().split(' ')))
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 모든 연결 요소의 개수 구하기
    for i in range(1, len(graph)):
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

    print(cnt)


