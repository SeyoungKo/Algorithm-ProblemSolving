# 시각
# 1. 정수 N이 입력되면
# 2. 00시 00분 00초부터 N시 59분 59초까지 3이 하나라도 포함된 시각을 모두 출력한다.

def time_in_three(n):
    count = 0
    for hour in range(n+1):
        for minutes in range(60):
            for sec in range(60):
                if '3' in str(hour) + str(minutes) + str(sec): # 시+분+초 조합의 수에서 3이 있을 때 count + 1
                    count += 1
    print(count)

if __name__ == '__main__':
    print("N: ", end='')
    n = int(input())
    time_in_three(n)