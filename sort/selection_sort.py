# 선택정렬 O(N**)
# 1. 가장 작은 수를 골라 맨 앞에 놓인 수와 비교해 바꾼다
# 2. 첫번째 인덱스 수를 제외한 나머지 중에서 가장 작은 수를 골라 두번째 인덱스 수와 비교해 바꾼다
# 3. n-1번 반복한다
# ->특정 리스트에서 가장 작은 데이터를 찾을 때 주로 사용된다. (데이터 수 많은 정렬 비효율적)

def selection_sort():
    arr = [7, 5, 1, 2, 5, 3, 9, 12, 11]

    for i in range(len(arr)):
        min_idx = i # 초기상태
        # i를 제외한 나머지 배열 값들 중 가장 작은 값 탐색
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)

if __name__ == '__main__':
    selection_sort()