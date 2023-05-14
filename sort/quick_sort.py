# 퀵 정렬 (NlogN)
# pivot = 가장 첫번째 원소
# start = pivot을 제외한 가장 첫번째 원소
# end = 가장 마지막 원소
# pivot보다 작은 수를 left+1하면서 저장하고 pivot보다 큰 수를 right-1하면서 저장한다.
# left와 right가 엇갈리는 시점에서 right인덱스의 배열 값과 pivot값을 swap한다.
# 엇갈리지 않았으면 left right인덱스 수를 swap한다.

# 재귀적으로 호출해서 구현가능하다.

def quick_sort(array, start, end):
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 작은수 / 큰수면 이동(+1, -1)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] > array[pivot]:
            right -= 1
        # 엇갈리면 작은 수 인덱스에 해당하는 값과 pivot인덱스 값을 swap한다.
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않으면 pivot보다 작은 수 데이터와 pivot보다 큰 수 데이터를 swap
        else:
            array[left], array[right] = array[right], array[left]

        quick_sort(array, start, right - 1)  # 1 ~ 왼(작은값)-1
        quick_sort(array, right + 1, end)  # 왼(작은값)+1 ~ 마지막 인덱

    return arr


# def python_quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]
#     remains = arr[1:]
#
#     left_remains = [n for n in remains if n <= pivot]
#     right_remains = [n for n in remains if n > pivot]
#
#     return python_quickSort(left_remains) + [pivot] + python_quickSort(right_remains)

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    remains = data[1:]
    max_arrs = [n for n in remains if n >= pivot]
    min_arrs = [n for n in remains if n < pivot]

    return quick_sort(min_arrs) + [pivot] + quick_sort(max_arrs)

if __name__ == '__main__':
    arr = [3, 7, 9, 1, 0, 3, 5, 3, 6, 2, 4, 3, 8]

    # arr = quick_sort(arr, 0, len(arr) - 1)
    # arr2 = python_quickSort(arr)
    print(quick_sort(arr))