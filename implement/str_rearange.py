# 문자열 재졍렬
# 문자열과 숫자가 섞인 라인에서 숫자는 더하고 문자열은 정렬되도록 한다.

if __name__ == '__main__':
    print('input:', end='')
    input_str = input()

    int_strs = 0
    strs = []

    for a in input_str:
        if a.isalpha():
            strs.append(a)
        else:
            int_strs += int(a)

    sorted(strs)
    if int_strs != 0:
        strs.append(str(int_strs))

    print(''.join(strs))