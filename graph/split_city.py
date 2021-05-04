# 도시 분할 계획
# 마을에 N개의 집과 집을 연결하는 M개의 길이 존재할 때
# 마을을 2개로 분리하고 (임의의 두 집 사이의 경로는 항상 존재하게 하면서)
# 길을 최소한으로 줄인다. (길의 합을 최소로 한다.)
# 길을 없애고 남은 나머지 길의 유지비 합의 최솟값을 출력한다.
# -> 크루스칼 알고리즘을 이용해 두 개의 최소 신장 트리로 분할한다.

def find_parent(parent, node):
    # 루트 노드가 아니라면 연결된 노드를 따라 루트 노드를 찾을 때까지 호출
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

# 연결된 두 개의 노드 중 더 큰 노드가 작은 노드의 부모가 됨
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

if __name__ == '__main__':
    print('N, M : ', end='')
    n, m = map(int, input().split())
    parent = [0] * (n + 1)

    # 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    result = 0
    edges = []
    for _ in range(m):
         a, b, c = map(int, input().split())
         edges.append((c, a, b)) # 비용 순으로 정렬하기 위해 cost를 앞에 놓음

    edges.sort() # 오름차순으로 정렬됨
    last = 0

    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않으면
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost # 가장 큰 비용이 저장됨

    # 마지막 노드와 연결되는 비용을 제외한 비용 (2개의 신장 트리로 분할)
    print('결과: ', result - last)