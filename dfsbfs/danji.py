# 단지번호붙이기 (2667번)

def dfs(x, y):
    global cnt
    # 범위에 벗어나는 경우 종료
    if x <= -1 or y <= -1 or x >= line or y >= line:
        return False

    if graph[x][y] == 1: # 1찾기
        graph[x][y] = 0 # 방문 완료
        cnt += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


if __name__ == '__main__':
    line = int(input())

    graph = [list(map(int, input())) for _ in range(line)]
    result = 0
    cnt = 0
    res = []

    for i in range(line):
        for j in range(line):
            if dfs(i, j):
                result += 1
                res.append(cnt)
                cnt = 0
    print(result)
    res.sort()
    for r in res:
        print(r)