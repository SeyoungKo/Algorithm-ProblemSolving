# 재귀 문제 풀이

# 자릿수의 합
def sum_digit(n):
    if n < 10:
        return n
    return sum_digit(n // 10) + n % 10

# 피보나치 수열
def factorial_rec(n):
    if n == 0:
        return 1
    return factorial_rec(n - 1) * n

# 회문 판별하기
def palindrome(word):
    if len(word) == 1:
        return '회문입니다'
    if word[0] == word[-1:]:
        return palindrome(word[1:-1])
    else:
        return '회문이 아닙니다'

# 홀/짝 판별
def oddeven(num):
    print(num)
    if num == 1:
        return num
    if num % 2 == 0:
        return oddeven(num // 2)
    else:
        return oddeven((3 * num) + 1)

# 1,2,3의 합으로 나타내는 경우의 수 구하기
def number_of_case(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return number_of_case(num - 1) + number_of_case(num - 2) + number_of_case(num - 3)

# 리스트 뒤집기
def reverse_list(param):
    if len(param) == 1:
        return param
    return reverse_list(param[:-1]) + param[-1:]

# 이진 탐색
def binary_search(target, n_list, start_idx, end_idx):
    '''
    :param element: 찾아야할 요소 (인덱스를 반환)
    :param n_list: 리스트
    :param start_idx: 첫번째 인덱스
    :param end_idx: 마지막 인덱스
    :return:
    '''
    if end_idx is None:
        end_idx = len(n_list) - 1

    middle_idx = (start_idx + end_idx) // 2

    if n_list[middle_idx] == target:
        return middle_idx
    elif n_list[middle_idx] > target: # 왼쪽으로
        binary_search(target, n_list, start_idx, middle_idx - 1)
    elif n_list[middle_idx] < target: # 오른쪽으로
        binary_search(target, n_list, middle_idx + 1, end_idx)

# 하노이 탑
def move_disk(num, start_peg, end_peg):
    '''
    :param num: 이동시킬 원판의 번호
    :param start_peg: 시작 기둥
    :param end_peg: 목표 기둥
    :return:
    '''
    print(f'{num}번째 원판을 {start_peg}번 기둥에서 {end_peg}번 기둥으로 이동')

# 마지막 원판이 시작 -> 목표 기둥으로 옮겨지면
# 임시 기둥에 있던 나머지 원판들이 임시 -> 목표 기둥으로 옮겨짐!
def hanoi(num, start_peg, end_peg):
    # 이동시킬 원판이 없으면 종료
    if num == 0:
        return
    else:
        # 임시 기둥 정의 (start_peg: 1, end_peg: 3, mid_peg: 2)
        mid_peg = 6 - start_peg - end_peg

        # 1. 가장 큰 원판만 남기고 나머지 원판을 임시 기둥으로 옮김
        # 2. 가장 큰 원판은 시작 기둥에서 목표 기둥으로 옮김
        # 3. 나머지 원판들을 임시 기둥에서 목표 기둥으로 옮김
        hanoi(num - 1, start_peg, mid_peg)
        move_disk(num, start_peg, end_peg)
        hanoi(num - 1, mid_peg, end_peg)

if __name__ == '__main__':
    n = 123456
    print(sum_digit(n))

    n_list = [5, 4, 3, 2, 1]
    n_list = reverse_list(n_list)
    print(n_list)

    print(binary_search(2, [3, 4, 2, 1, 5], 0, None))

    num = 3
    start_peg = 1
    end_peg = 3
    hanoi(num, start_peg, end_peg)

    word = 'level'
    print(palindrome(word))

    oddeven(3)
    print(number_of_case(5))
