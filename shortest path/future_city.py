# 미래도시
# 방문 판매원이 1부터 회사 사이를 이동하는 최소 이동 시간을 계산한다. (한번 경로를 방문할 때 +1의 시간)
# N : 전체 회사 개수, M : 경로 개수
# M개 만큼 연결된 두 회사의 번호(X, K)가 주어진다.

import sys
INF = int(1e9)
input = sys.stdin.readline

if __name__ == '__main__':
    # 노드의 개수와 간선의 개수를 입력받고
    n, m = map(int, input().split()) # n : 회사 개수 (노드) m : 경로 개수 (간선)

    # 2차원 리스트를 만들어 무한으로 초기화
    graph = [[INF] * (n+1) for _ in range(n+1)]

    # 자기 자신-자기 자신의 비용 0으로 세팅
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    # 각 간선의 정보를 입력받아 초기화
    for _ in range(m):
        a, b = map(int, input().split()) # 연결된 두 회사의 번호
        # 두 회사가 연결되어 있다면 1만큼 시간으로 이동
        graph[a][b] = 1
        graph[b][a] = 1

    # 거쳐갈 노드 x와 최종 목적지 노드 k 입력받기
    x, k = map(int, input().split())

    # 플로이드 워셜 알고리즘 수행
    for i in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    # 판매원 A가 x까지 이동하는 최단 경로
    distance = graph[1][k] + graph[k][x]

    # 조건문에 따라 도달할 수 있는지 / 없는지
    if distance >= INF:
        print("-1")
    else:
        print(distance)