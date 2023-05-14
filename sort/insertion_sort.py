<<<<<<< Updated upstream
# 삽입정렬
# 두번째 배열 값부터 마지막 값까지 차례대로 오름차순으로 정렬되는 구간에 삽입한다  O(N**)
=======
# 삽입정렬 O(n²)
# 두번째 배열 값부터 마지막 값까지 차례대로 오름차순으로 정렬되는 구간에 삽입한다
>>>>>>> Stashed changes

def insertion_sort():
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                continue
    print(arr)

    
 if __name__ == '__main__':
    insertion_sort()
