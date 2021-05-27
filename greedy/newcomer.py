# 신입사원 (1946번)
import sys

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        m = int(input())
        first = sorted([list(map(int, sys.stdin.readline().strip().split()))
                        for i in range(m)], key=lambda x: x[0])

        cnt = 1
        top = first[0][1] # 서류점수 1등인 사람의 인터뷰점수
        for j in range(1, len(first)):
            if first[j][1] < top:
                top = first[j][1]
                cnt += 1

        # print(len(res) + 1)
        sys.stdout.write('{}\n'.format(cnt))
