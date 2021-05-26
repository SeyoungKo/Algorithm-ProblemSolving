# ATM (11399번)

if __name__ == '__main__':
    n = int(input())
    person = list(map(int, input().split(' ')))
    person.sort(reverse=False)

    acc, res = 0, 0
    for p in person:
        acc += p
        res += acc

    print(res)

