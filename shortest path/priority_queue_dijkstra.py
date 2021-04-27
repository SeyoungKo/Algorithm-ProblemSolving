# 우선순위 큐를 이용한 다익스트라
# 1. start 노드를 제외한 노드의 최단 거리를 무한으로 설정한다.
# 2. 우선순위 큐(튜플 형식의 (거리, 노드번호))에 start 노드를 넣는다. (이때 start 노드의 거리는 0이다.)
# 3. 우선순위 큐는 현재 노드 기준 최단거리 순으로 정렬된다. (최단거리 기준으로 우선순위 적용됨)
# 4. 거리가 가장 짧은 노드 순서대로 정렬된 우선순위 큐 순서대로 처리한다. (이미 방문한 노드라면 무시하고 다음 우선순위 큐를 처리한다.)
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 최단 경로(0), 노드 번호
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q) # 가장 dist(최단 거리)가 짧은 노드 순서대로 pop
        if distance[node] < dist: # now 노드가 이미 처리된 적 있는 노드라면 무시
            continue

        for i in graph[node]: # now 노드와 연결된 다른 인접 노드 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # distance[i[0]]: i[0]노드의 최단거리가 이미 저장되어 있는 상태
                distance[i[0]] = cost # 저장된 최단거리보다 현재 노드를 거친 더 짧은 거리(cost)로 저장
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    print('n, m: ', end='')
    n, m = map(int, input().split()) # 노드, 간선

    print('start: ', end='')
    start = int(input()) # 시작 노드 번

    distance = [INF] * (n+1) # 노드의 최종 최단거리 저장 테이블
    graph = [[] for _ in range(n+1)] # 그래프 초기화

    for _ in range(m):
        a, b, c = map(int, input().split()) # 노드 번호, 연결 노드, 거리
        graph[a].append((b,c)) # 노드에 연결할 노드 번호와 거리를 저장

    dijkstra(start)

    for i in range(1, n+1):
        if distance[i] == INF:
            print('INFINITY!')
        else:
            print(distance[i])