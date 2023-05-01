def target_number(idx, prev, numbers, target):
    if idx >= len(numbers):
        if target == prev:
            return 1
        return 0

    sum1 = prev + numbers[idx]
    sum2 = prev - numbers[idx]

    return target_number(idx + 1, sum1, numbers, target) + target_number(idx + 1, sum2, numbers, target)

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    result = 0

    result += target_number(1, numbers[0], numbers, target)
    result += target_number(1, -numbers[0], numbers, target)

    print(result)