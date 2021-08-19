# Unique In Order

def unique_in_order(iterable):
    result = []
    for item in iterable:
        if len(result) < 1 or not item == result[len(result) - 1]:
            result.append(item)
    return result


if __name__ == '__main__':
    strs1 = 'AAAABBBCCDAABBB'
    strs2 = 'ABBCcAD'
    strs3 = ['1, 2, 2, 3, 3']

    print(unique_in_order(strs3))