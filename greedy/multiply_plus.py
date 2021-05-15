# 곱하기 혹은 더하기
# 왼쪽부터 오른쪽 방향으로 숫자를 확인해 X 혹은 +로 만들 수 있는 가장 큰 수를 구해본다.
if __name__ == '__main__':
    print('num: ', end='')
    num = list(map(int, input()))
    result = 0

    for i in range(len(num)):
        if num[i] <= 1 or result <= 1:
            result += num[i]
        else:
            result *= num[i]
    print(result)