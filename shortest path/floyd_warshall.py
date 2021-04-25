# 플로이드 워셜 알고리즘
# 다익스트라 알고리즘 - 한 지점에서 다른 특정 지점까지 최단 경로 구하기
# 플로이드 워셜 알고리즘 - 모든 지점에서 다른 모든 지점까지의 모든 최단 경로 구하기
# 1. n개의 노드가 주어질 때 1번 노드를 제외하고 a 노드 -> 타겟노드 -> b 노드로 가는 비용을 확인한다.
# 2. 노드의 최단 경로를 갱신하고 (a-> 현재 타겟 노드로 가는 최소 비용, 현재 타겟 노드 ->b로 가는 비용을 비교해 더 작은 값으로 갱신)
# 3. n개의 노드(2번..3번.. n번) 각각에 대해 반복한다. (n번 수행)
INF = int(1e9)

if __name__ == '__main__':
    n, m = map(int, input().split()) # 노드의 개수와 간선의 개수
    graph = [[INF] * (n+1) for _ in range(n+1)] # 각 노드, 각 노드와 연결된 노드의 최단 거리를 저장하는 2차원 리스트

    # 자기 자신과 연결되는 비용은 0으로 초기화 (0*0, 1*1, n*n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    # 간선 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split()) # 노드a에서 노드b로 가는 거리 비용 c
        graph[a][b] = c

    # 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1): # 타겟 노드 (a-b 경로에서 지나가는 노드)
        for a in range(1, n+1): # a 노드
            for b in range(1, n+1): # b 노드
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 결과 출력
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print('INFINITY', end=' ')
            else:
                print(graph[a][b], end=' ')
        print()