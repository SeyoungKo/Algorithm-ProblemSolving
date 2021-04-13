# 개미전사
# 입력받은 배열 개수만큼 탐색하면서 식량이 가장 최대가 되도록 더한다. (인접하는 원소는 X)
def getfood(store):
    d = [0] * 100000

    d[0] = store[0]
    d[1] = max(store[0], store[1])

    for i in range(2, len(store)):
        d[i] = max(d[i-1], d[i-2] + store[i])

    print(d[len(store)-1])

if __name__ == '__main__':
    print("n :", end='')
    n = int(input())

    store = list(map(int, input().split()))
    getfood(store)