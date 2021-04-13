# 바닥공사

def construction(n):
    d = [0] * 1000

    # 덮개를 채울수있는 공간이 2*1, 2*2
    d[1] = 1 # 2*1 - 1가지방법
    d[2] = 3 # 2*2 - 3가지방법

    for i in range(3, n+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796.796

    return d[n]

# 1 2 3 4
# 3 2 1 0
# 1 3 4 5

if __name__ == '__main__':
    print("n: ", end='')
    n = int(input())

    result = construction(n)
    print(result)
