# 타겟 넘버
def dfs(prev, index, numbers, target):
    ans = 0
    if index >= len(numbers):
        if target == prev:
            return 1
        return 0

    cur1 = prev + numbers[index]
    cur2 = prev - numbers[index]

    # +, - 두가지 경우의 수
    ans += dfs(cur1, index+1, numbers, target)
    ans += dfs(cur2, index+1, numbers, target)

    return ans

def solution(numbers, target):
    answer = 0

    def dfs(prev, index, numbers, target):
        answer = 0

        if index >= len(numbers):
            if target == prev:
                return 1
            return 0

        cal1 = prev + numbers[index]
        cal2 = prev - numbers[index]

        answer += dfs(cal1, index + 1, numbers, target)
        answer += dfs(cal2, index + 1, numbers, target)

        return answer

    current = numbers[0]
    answer += dfs(current, 1, numbers, target)
    answer += dfs(-current, 1, numbers, target)

    return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = 0

    current = numbers[0]
    answer += dfs(current, 1, numbers, target)
    answer += dfs(-current, 1, numbers, target)

    print(answer)