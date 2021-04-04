# 그래프
# 1. 인접행렬 방식 : 2차원 배열로 그래프 연결관계 표현
# 2. 인접리스트 방식 : 리스트로 그래프 연결관계 표현

# 인접행렬 방식
def adj_matrix():
    INF = 999999999  # 연결되어 있지 않은 노드끼리 무한의 비용이라고 작성할 때 사용
    # 3*3 그래프일 때 1,2,3 노드의 연결상태
    graph = [
        [0, 1, 2],
        [7, 0, INF],
        [5, INF, 0]
    ]
    print(graph)


# 인접리스트 방식
def adj_list():
    graph = [[] for _ in range(3)]

    # 노드 0에 연결된 노드 정보 저장 (노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    graph[1].append((0, 7))

    graph[2].append((0, 5))
    print(graph)


if __name__ == '__main__':
    adj_matrix()
    adj_list()
