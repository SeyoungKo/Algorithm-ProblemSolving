# 깊이우선탐색 (dfs)
# 1. 가장 깊숙이 위치하는 노드에 닿을때까지 노드를 스택에 저장한다. (작은 숫자 우선)
# 2. 더 이상 확인할 노드가 없으면 뒤로 한칸씩 이동하면서 스택을 pop한다
# 3. 스택에 노드가 없을 때까지 탐색한다.

def dfs(graph, v, visited):
    # 현재 방문한 노드를 True처리
    visited[v] = True
    print("\ndfs search node:", v,"번째 배열")
    print("--- connected node --- :", graph[v])

    for i in graph[v]:
        if not visited[i]:
            print("push stack (not visited) :", i)
            dfs(graph, i, visited) # 재귀적으로 호출하므로 만약 visited[i] 이미 방문했고 더이상 경로가 없다면
            # 자동적으로 이전 graph[v]의 i이후 인덱스를 탐색하게 된다. (=더이상 확인할 노드가 없으면 이전 노드로 이동)
            # 재귀를 계속 호출했는데도 끝까지 방문하지 않은 인덱스가 없다면 종료
        print("이미 탐색완료한 노드:", i)

def stack_dfs(graph, start):
    stack, visited = [], []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

if __name__ == '__main__':
    # graph[i]의 노드를 방문한 노드인지 아닌지 탐색한다
    # graph[i] 노드 중 방문하지 않은 노드를 만나면 stack에 저장하고
    # graph[stack.top()]의 노드로 이동한다
    # graph[stack.top()] 노드 중 방문하지 않은 노드를 만나면 stack에 저장하고 반복한다
    # 만약 graph[...] 노드 중 방문하지 않은 노드가 없으면 pop한다
    # 이후 stack의 graph[top]의 노드 중 방문하지 않은 노드가 있는지 반복하고
    # stack이 빌 때까지 반복한다

    visited = [False] * 9
    # 깊이우선탐색이라서
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    graph_alpha = dict()
    graph_alpha['A'] = ['B', 'C']
    graph_alpha['B'] = ['A', 'D']
    graph_alpha['C'] = ['A', 'G', 'H', 'I']
    graph_alpha['D'] = ['B', 'E', 'F']
    graph_alpha['E'] = ['D']
    graph_alpha['F'] = ['D']
    graph_alpha['G'] = ['C']
    graph_alpha['H'] = ['C']
    graph_alpha['I'] = ['C', 'J']
    graph_alpha['J'] = ['I']

    # dfs(graph, 1, visited)
    print(stack_dfs(graph_alpha, 'A'))