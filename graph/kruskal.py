# 크루스칼 알고리즘
# 최소한의 비용으로 신장 트리를 찾을 때 (ex- 모든 도시를 연결할 때, 최소 비용으로 연결하려면 ?)
# 크루스칼 알고리즘은 최소 신장 트리 알고리즘의 한 종류

# 1. 간선 데이터를 오름차순으로 정렬
# 2. 간선을 확인하며 사이클이 발생되는지 확인
# 3. 모든 간선에 대해 사이클이 발생되지 않으면 최소 신장 트리에 포함시키고 사이클이 발생되는 경우 포함시키지 않는다.
def find_parent(parent, node):
    # 루트 노드가 아니라면 연결된 노드를 따라 루트 노드를 찾을 때까지 호출
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

# 두 원소가 속한 집합 (연결된 두 개의 노드 중 더 큰 노드가 작은 노드의 부모 노드가 됨)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

if __name__ == '__main__':
    print("n, m: ", end='')
    n, m = map(int, input().split()) # 노드, 간선
    result = 0 # 최소 신장 트리를 만드는데 필요한 최소 비용
    parent = [0] * (n+1)

    # 부모노드를 자기 자신으로 초기화
    for i in range(1, n+1):
        parent[i] = i

    edges = []
    # 연결 정보 입력
    for i in range(m):
        a, b, c = map(int, input().split()) # 노드 a - 노드 b, 연결 비용
        edges.append((c, b, a)) # 비용을 기준으로 정렬하기 위해 c를 맨 앞으로

    # 간선을 오름차순으로 정렬
    edges.sort()

    # 간선이 짧은 순서대로 탐색
    for edge in edges:
        cost, b, a = edge
        # 사이클이 생기지 않는 경우(루트 노드가 같지 않은 경우)에만 최소 신장 트리에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print("최소 비용: ", result)