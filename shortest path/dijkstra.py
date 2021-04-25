# 간단한 다익스트라 알고리즘 구현
import sys
input = sys.stdin.readline  # input을 더 빠르게 동작


# 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 번호를 반환
def get_smallest_node():
    min_value = INF
    idx = 0  # 최단 거리가 가장 짧은 노드의 인덱스
    for i in range(1, n + 1):  # 노드 1부터 노드 n까지
        if distance[i] < min_value and not visited[i]:  # 방문하지 않은 노드면서 무한이 아닌 수
            min_value = distance[i]  # 최단거리가 짧은 노드 값 갱신
            idx = i  # 최단거리 노드 인덱스 갱신
    return idx


def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node() # 현재까지 최단 거리가 가장 짧은 노드의 인덱스로 방문처리
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1] # 현재 노드와 연결된 다르 노드를 확인
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost


if __name__ == '__main__':
    INF = int(1e9)  # 무한(10억)

    n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
    start = int(input())  # 시작 노드 번호
    graph = [n for i in range(n + 1)]  # 노드 번호를 인덱스로 바로 사용하기 위해 n+1 크기 만큼 할당
    visited = [False] * (n + 1)  # 노드 방문 여부 확인
    distance = [INF] * (n + 1)  # 최단거리 테이블을 모두 초기화

    # 간선 정보 입력받기
    for _ in range(m):
        a, b, c = map(int, input().split())  # 노드 a에서 노드 b로 가는 비용이 c
        graph[a].append((b, c))

    # 다익스트라 수행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n+1):
        if distance[i] == INF: # 무한대인 경우
            print('INFINITY', end='\t')
        else:
            print(distance[i], end='\t')