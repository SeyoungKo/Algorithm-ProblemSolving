# 팀 결성 (서로소 집합 이용)
# n번까지 학생들이 있을 때 팀을 합치거나 (0 a, b) 같은 팀 여부를 확인한다. (1, a, b)
# 같은팀 여부 확인 연산에 대해서는 YES 혹은 NO 결과를 출력한다.

def find_parent(parent, node):
    # 루트 노드가 아니라면 연결된 노드를 탐색해 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[node] != node :
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

# 두 원소가 속한 집합을 합치
def union_parent(parent, a, b):
    a = find_parent(parent, a) # a노드의 부모 탐색
    b = find_parent(parent, b) # b노드의 부모 탐색
    if a < b:
        parent[a] = b
    else:
        parent[a] = b

if __name__ == '__main__':
    print('n, count: ', end='')
    n, count = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 부모를 자기 자신으로 초기화
    for i in range(n + 1):
        parent[i] = i

    for i in range(count):
        op, a, b = map(int, input().split())
        # 각 노드를 같은 팀으로 합치기
        if op == 0:
            union_parent(parent, a, b)
        # 같은 팀 여부 확인기
        elif op == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                print('YES')
            else:
                print('NO')