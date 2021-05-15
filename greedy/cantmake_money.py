# 만들 수 없는 금액
# N개의 동전이 주어질 때 만들 수 없는 최소금액 구하
if __name__ == '__main__':
    print('N: ', end='')
    n = input()

    print('num: ', end='')
    num = map(int, input().split(' '))
    num = sorted(num)

    val = 0
    target = 1기

    for n in num:
        if n <= target:
            target += n # target을 누적하면서 가지고 있는 돈이 target보다 크면 break
        else:
            break

    print(target)



