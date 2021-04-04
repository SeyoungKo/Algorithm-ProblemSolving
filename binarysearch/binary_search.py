# 이진탐색
# 1. 재귀함수를 이용하는 방법
# 2. 반복문을 이용하는 방법

def bs_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2  # 소수점 이하 수 버리고 정수로 저장

    # target값과 같은 값을 찾은 경우 (가운데 값 반환)
    if array[mid] == target:
        return mid
    # target값이 array[mid]보다 작은 경우
    elif array[mid] > target:
        return bs_recursive(array, target, start, mid - 1)
    # target값이 array[mid]보다 큰 경우
    elif array[mid] < target:
        return bs_recursive(array, target, mid + 1, end)


def bs_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # target값과 같은 값을 찾은 경우
        if array[mid] == target:
            return mid
        # target값이 array[mid]보다 작은 경우
        elif array[mid] > target:
            end = mid - 1
        # target값이 array[mid]보다 큰 경우
        elif array[mid] < target:
            start = mid + 1
        else:
            return None


if __name__ == '__main__':
    # 원소 개수, 찾으려는 문자열 입력
    n, target = map(int, input().split())
    # n개만큼 배열의 원소를 입력
    array = list(map(int, input().split()))

    # result = bs_recursive(array, target, 0, n-1)
    result = bs_loop(array, target, 0, n - 1)
    if result is None:
        print("원소가 존재하지 않음")
    else:
        print(result, "번째 인덱스")
