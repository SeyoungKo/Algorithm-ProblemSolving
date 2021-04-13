# 다이나믹 프로그래밍
# 1. 탑다운 방식(메모이제이션) : 재귀함수 사용 - 하향식
# 2. 보텀업 방식(DP 테이블 이용) : 반복문 사용 - 상향식
# 메모이제이션 : 이전에 계산한 결과를 기록해 놓는 것 (다이나믹프로그래밍을 위해 쓰지 않을 수도 있다.)

def bottom_up():
    d = [0] * 100 # 결과 저장용 DP 테이블

    d[1] = 1
    d[2] = 1
    n = 99

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])

def top_down(x):
    d = [0] * 100 # 메모이제이션

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = top_down(x-1) + top_down(x-2)
    return d[x]

if __name__ == '__main__':
    # bottom_up()
    print(top_down(5))