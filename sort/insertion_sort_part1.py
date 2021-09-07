# Insertion Sort - Part1

def insertionSort1(n, arr):
    target = arr[-1]
    idx = n - 2

    while (target < arr[idx]) and (idx >= 0):
        arr[idx + 1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1

    arr[idx + 1] = target
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = 5
    arr = [2, 4, 6, 8, 3]
    insertionSort1(n, arr)