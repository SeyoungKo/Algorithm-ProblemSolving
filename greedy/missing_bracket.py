# 잃어버린 괄호 (1541번)
# -을 만나기전까지 모두 더하고 -이후의 수를 모두 뺀다.

if __name__ == '__main__':
    calc = input().split('-')
    res = 0
    print(calc)
    for plus in calc[0].split('+'):
        res += int(plus)

    for minus in calc[1:]:
        for j in minus.split('+'):
            res -= int(j)

    print(res)


