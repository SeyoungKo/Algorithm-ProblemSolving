# 우선순위 큐를 이용한 다익스트라
# 1. start 노드를 제외한 노드의 최단 거리를 무한으로 설정한다.
# 2. 우선순위 큐(튜플 형식의 (거리, 노드번호))에 start 노드를 넣는다. (이때 start 노드의 거리는 0이다.)
# 3. 우선순위 큐는 현재 노드 기준 최단거리 순으로 정렬된다. (최단거리 기준으로 우선순위 적용됨)
# 4. 거리가 가장 짧은 노드 순서대로 정렬된 우선순위 큐 순서대로 처리한다. (이미 방문한 노드라면 무시하고 다음 우선순위 큐를 처리한다.)
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한 설정

if __name__ == '__main__':
    # 노드의 개수, 간선의 개수
    n, m = map(int, input().split())
    # 시작 노드 번호
    start = int(input())

    # 각 노드에 연결되어 있는 노드 정보를 담는 리스트
    graph = [[] for i in range(n+1)]  # 인덱스로 바로 노드에 접근할 수 있도록 n+1만큼 할당
    # 최단 거리 테이블 초기화
    distance = [INF] * (n+1)

    # 모든 간선 정보 입력받기
    for _ in range(m):
        a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c
        graph[a].append((b, c)) # a번 노드의 연결 정보 저장


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # start 노드 초기화 (거리 0, start 노드 번호)
    distance[start] = 0 # start 노드 최단거리 0으로 초기화

    while q: # 큐가 비어있지 않다면
        dist, target_n = heapq.heappop(q) # 가장 최단 거리, 노드 번호를 pop
        if distance[target_n] < dist: # 이미 처리된 적 있는 노드라면 무시
            continue

        # 현재 노드와 연결된 인접한 노드들을 확인
        for i in graph[target_n]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐 노드(i[0])로 이동하는 거리가 더 짧으면
                distance[i[0]] = cost # 연결된 노드의 최단거리를 cost로 갱신한다.
                heapq.heappush(q, (cost, i[0]))

dijkstra(start) # 다익스트라 수행

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

