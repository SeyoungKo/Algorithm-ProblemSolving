# 계수 정렬 (데이터 개수가 N, 최댓값이 K일때 O(N+K))
# 1,000,000을 넘지 않는 정수형 데이터를 정렬할 때 효과적이다. (빠른 정렬, 간단한 원리)
# 가장 큰 데이터와 가장 작은 데이터의 차이가 크다면 사용 불가능

# 1. 정렬할 수 +1 크기만큼의 arr 배열 생성
# 2. 정렬할 수가 한번 나올 때마다 정렬할 수 arr 인덱스 +1 (ex 정렬할 수 5 -> arr[5] += 1)
# 3. arr에 저장된 수를 차례대로 꺼내면 완성 (정렬할 수가 중복되어 2이상인 경우 여러번 나열)

def count_sort(array):

    count = [0] * (max(array) + 1)
    res = [0] * (max(count))

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)
    print(res)


if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    count_sort(array)