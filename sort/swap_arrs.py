# 두 배열의 원소 교체
# 두 배열이 주어질 때 최대 k번의 바꾸기 연산을 수행해 배열 A의 합이 최대가 되도록 한다.

def swap_arrs(a, b, m):
    max_val = 0
    before = 0

    for arr in a:
        before += arr

    for i in range(m):
        a[i], b[i] = b[i], a[i]

    for arr in a:
        max_val += arr

    print("before:", before, "After:", max_val)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    swap_arrs(a, b, m)