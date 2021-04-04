# 파이썬 정렬 라이브러리
# 합병정렬을 기반으로 만들어짐 (퀵정렬보다 느리지만 최악의 경우에도 O(NlogN))
# 리스트나 딕셔너리 형태를 입력받아 출력

def sortLib(arr):
    # 1. sorted : 새로운 변수에 저장
    result = sorted(arr)
    print(result)

    # 2. sort : 기존 배열에 정렬해서 바로 저장
    arr.sort()
    print(arr)

    # 기본 정렬 (숫자는 오름차순으로, 문자열은 알파벳 각각 리스트에 저장)
    result = sorted((3,5,1,2))
    result = sorted("hello")

    array = {'바나나': 2, '사과': 5, '당근': 1}
    # key값 기준으로 정렬
    result = sorted(array.items(), key=lambda x: x[1])

    # n번째 문자열 기준으로 정렬
    array = ['apple', 'banana', 'carrot', 'melon']
    result = sorted(array, key=lambda x: x[1]) # 2번째 문자 기준 정렬

    # 여러 차원 리스트 정렬 (첫번째 숫자를 기준으로 정렬됨)
    array = [[4, 5, 6], [2, 3, 1], [1, 2, 3]]
    result = sorted(array)
    print(result)

if __name__ == '__main__':
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    sortLib(arr)