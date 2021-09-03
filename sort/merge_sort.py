# 병합 정렬 O(nlogn)
# 재귀호출을 사용한 정렬 알고리즘
# 1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분으로 나눈다 (재귀함수)
# 2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다
# 3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다

def split(data):
    # 재귀적으로 호출해 리스트를 두 부분으로 계속 쪼개는 함수
    if len(data) <= 1:
        return data
    mid = int(len(data) / 2)
    left = split(data[:mid])
    right = split(data[mid:])
    return merge_sort(left, right)

def merge_sort(left, right):
    # 두 부분으로 나눠진 데이터를 합치는 함수
    # 1. 각각 나눠진 두 리스트의 인덱스 값으로 비교 (더 작은 값을 넣고)
    # 2. 남은 값은 가장 마지막에 추가
    left_idx, right_idx = 0, 0
    merge_list = []

    # case 1 : left/right아직 남아있을 때
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] > right[right_idx]:
            merge_list.append(right[right_idx])
            right_idx += 1
        else:
            merge_list.append(left[left_idx])
            left_idx += 1

    # case 2 : left만 남았을 때
    while len(left) > left_idx:
        merge_list.append(left[left_idx])
        left_idx += 1

    # case 3 : right만 남았을 때
    while len(right) > right_idx:
        merge_list.append(right[right_idx])
        right_idx += 1

    return merge_list

if __name__ == '__main__':
    data = [3, 4, 1, 3]
    print(split(data))