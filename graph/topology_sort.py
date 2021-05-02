# 위상 정렬 (정렬 알고리즘)
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열한다.
# ex) 선수과목을 고려한 학습 순서 (자료구조 -> 알고리즘 -> 고급 알고리즘)

# 1. 진입차수(타겟 노드를 가리키는 노드가 없는 경우 (주로 첫번째 시 노드))가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지
# 3. 큐에서 원소를 꺼내 타겟 노드에서 출발하는 간선을 그래프에서 제거한다.
# 4. 새롭게 진입차수가 0이된 노드를 큐에 넣는다.

from collections import deque

# 위상 정렬 함수
def topology_sort():
    q = deque()
    result = []  # 최종 결과를 담는 리스

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지
    while q:
        now = q.popleft()  # 큐에서 노드 한개 pop
        result.append(now)

        # now와 연결된 노드들의 간선 끊기 (연결된 노드의 진입 차수 -1)
        for i in graph[now]:
            indegree[i] -= 1
            # now와 연결된 노드들 중 진입 차수가 새롭게 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    return result


# 위상 정렬 결과 출력
def print_node(result):
    print('위상 정렬 결과: ', end='')
    for node in result:
        print(node, end='\t')


if __name__ == '__main__':

    print("n, m:", end='')
    n, m = map(int, input().split())

    # 모든 노드의 진입차수 0으로 초기화
    indegree = [0] * (n + 1)

    # 각 노드에 연결된 간선을 담는 리스트 초기화
    graph = [[] for _ in range(n + 1)]

    # 모든 간선 정보를 입력받기
    for _ in range(m):
        a, b = map(int, input().split())  # 노드 a-노드 b
        graph[a].append(b)
        # 진입차수 증가 (b로 들어오는 노드의 개수)
        indegree[b] += 1

    result = topology_sort()
    print_node(result)