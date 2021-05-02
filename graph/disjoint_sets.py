# 서로소 집합
# 공통 원소가 없는 두 집합
# 0. 각 노드는 노드 번호, 부모 노드 번호를 포함한다.
# 1. 각 노드가 자기 자신을 부모로 가지도록 설정 (union)
# 2. 연결된 노드들을 확인하고 노드 번호가 더 작은 부모노드가 부모가 되도록 변경 (union)
# 3. 연결된 노드의 부모 노드가 더 이상 없을 때까지 (부모 노드가 연결된 노드 자기 자신이 될 때까지) 재귀적으로 거슬러 올라간다.

# 경로 압축 (바로 부모 노드 할당)
def find_parent_rec(parent, n):
    if parent[n] != n:
        parent[n] = find_parent_rec(parent, parent[n])
        print('\n')
    return parent[n]


# 경로 압축 x (시간 복잡도 증)
def find_parent(parent, n):
    if parent[n] != n:
        return find_parent(parent, parent[n])
    else:
        return n


def union_parent(parent, a, b):
    # a = find_parent(parent, a)
    # b = find_parent(parent, b)
    a = find_parent_rec(parent, a)
    b = find_parent_rec(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    n, m = map(int, input().split())  # 노드의 개수와 간선의 개수
    parent = [0] * (n + 1)

    # 부모 테이블에서 부모 노드 번호를 자기 자신으로 초기화
    for i in range(n + 1):
        parent[i] = i

    # 노드의 연결 정보 입력
    for i in range(m):
        a, b = map(int, input().split())
        union_parent(parent, a, b)  # union 수행

    # 각 노드가 속한 집단 출력 (더 이상 연결할 노드가 없을 때의 부모 노드로 집단을 구분)
    print('각 노드가 속한 집단', end='')
    for i in range(1, n + 1):
        print(find_parent_rec(parent, i), end=' ')
    print()

    # 부모 테이블 내용 출력
    print('각 노드의 부모 테이블', end='')
    for i in range(1, n + 1):
        print(parent[i], end=' ')
