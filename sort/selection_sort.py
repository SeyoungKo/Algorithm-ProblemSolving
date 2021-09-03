# 선택정렬 O(n²)
# 최소값을 선택!
# 1. 가장 작은 수를 골라 맨 앞에 놓인 수와 비교해 바꾼다
# 2. 첫번째 인덱스 수를 제외한 나머지 중에서 가장 작은 수를 골라 두번째 인덱스 수와 비교해 바꾼다
# 3. n-1번 반복한다
# ->특정 리스트에서 가장 작은 데이터를 찾을 때 주로 사용된다. (데이터 수 많은 정렬 비효율적)

def selection_sort(data):
    for base in range(len(data) - 1):
        min_idx = base
        for i in range(base + 1, len(data)):
            if data[min_idx] > data[i]:
                min_idx = i
        data[min_idx], data[base] = data[base], data[min_idx]
    return data

if __name__ == '__main__':
    arr = [7, 5, 1, 2, 5, 3, 9, 12, 11]
    print(selection_sort(arr))