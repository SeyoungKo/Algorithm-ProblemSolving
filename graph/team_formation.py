# 팀 결성
# n번까지 학생들이 있을 때 팀을 합치거나 (0 a, b) 같은 팀 여부를 확인한다. (1, a, b)
# 같은팀 여부 확인 연산에 대해서는 YES 혹은 NO 결과를 출력한다.

def check_team(a, b):
    if b in graph[a]:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    print("N, count: ", end='')
    n, count = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    # 연결 정보 입력받기
    for i in range(count):
        op, a, b = map(int, input().split())
        # 같은 팀으로 합치기
        if op == 0:
            graph[a].append(b)
        # 같은 팀 여부 확인
        elif op == 1:
            print(check_team(a, b))