# 미로 찾기
# bfs(최단 경로찾기)를 이용해 n,m 지점까지 최단 경로를 계산한다.
# 1이면 이동 가능, 0이면 이동 불가능한 좌표
# 현재 좌표에서 상,하,좌,우로 이동하면서 +1한다. (최종 좌표가 최단 경로를 계산한 값이 되도록)

from collections import deque

def find_maze(graph, x, y, n, m, visited):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1 # 현재 (graph[nx][ny]는 이전 노드 (graph[x][y])에 +1한 것
                queue.append((nx, ny))

    print(graph[n-1][m-1])

if __name__ == '__main__':
    print("n, m: ", end='')
    n, m = map(int, input().split())
    graph = []
    print("{} x {}: ".format(n, m))

    # 인덱스 0은 []로 초기화, 이외는 모두 이차원 리스트로 초기
    # visited = [[] if i == 0 else [False]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]

    for i in range(n):
        graph.append(list(map(int, input().split())))

    find_maze(graph, 0, 0, n, m, visited)