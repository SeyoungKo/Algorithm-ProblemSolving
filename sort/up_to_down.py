# 위에서 아래로
# 내림차순 정렬하기

def move_up_to_down(arr):
    array = reversed(sorted(arr))
    # sorted(arr, reverse=True)

    for arr in array:
        print(arr, end=' ')

if __name__ == '__main__':
    print("n :", end='')
    n = int(input())

    nums = []
    for _ in range(n):
        m = int(input())
        nums.append(m)

    move_up_to_down(nums)