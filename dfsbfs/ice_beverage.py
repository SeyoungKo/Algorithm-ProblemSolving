# 음료수 얼려먹기
# dfs를 이용해 0 모두 탐색한다
# 1. 특정 좌표의 상, 하, 좌, 우를 살펴보고 값이 0이면서 아직 방문하지 않은 지점을 방문한다.
# 2. 방문한 지점에서 계속 상하좌우를 살피면서 방문을하면 연결된 모든 지점을 방문할 수 있다.
# 3. 모든 노드에 반복하고 방문하지 않은 노드의 개수를 센다.

# def dfs(graph, x, y, n, m):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0: # 비어있는 곳
#         graph[x][y] = 1
#         dfs(graph, x-1, y, n, m) # 좌
#         dfs(graph, x+1, y, n, m) # 우
#         dfs(graph, x, y-1, n, m) # 하
#         dfs(graph, x, y+1, n, m) # 상
#         return True
#     return False
#
#
# def doit_ice(graph, n, m):
#     num = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(graph, i, j, n, m) is True:
#                 num += 1
#     print("{}개의 얼음을 만들었다".format(num))
#
#
# def init_ice_mold(n, m):
#     ice_mold = []
#     print("{} x {}만큼 얼음 만들기: ".format(n, m))
#     for _ in range(n):
#         ice_mold.append(list(map(int, input().split())))
#
#     return ice_mold

if __name__ == '__main__':
    # print("n, m: ", end='')
    # n, m = map(int, input().split())
    #
    # graph = init_ice_mold(n, m)
    # doit_ice(graph, n, m)
    n, m = map(int, input().split())
    graph = []
    result = 0

    def dfs(x, y, n, m):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x + 1, y, n, m)
            dfs(x - 1, y, n, m)
            dfs(x, y + 1, n, m)
            dfs(x, y - 1, n, m)
            return True

        return False

    for _ in range(n):
        graph.append(list(map(int, input())))

    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m) == True:
                result += 1

    print(result)

