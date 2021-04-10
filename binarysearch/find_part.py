# 부품찾기

def search_parts(saved, finds, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if saved[mid] == finds:
        return mid

    elif saved[mid] < finds:
        return search_parts(saved, finds, mid + 1, end)

    elif saved[mid] > finds:
        return search_parts(saved, finds, start, mid - 1)


if __name__ == '__main__':
    print("N: ", end='')
    n = int(input())
    saved = list(map(int, input().split()))
    sorted(saved)

    print("M: ", end='')
    m = int(input())
    finds = list(map(int, input().split()))
    sorted(finds)

    answers = []
    for i in range(m):
        answers.append(search_parts(saved, finds[i], 0, len(saved) - 1))

    strs = ''
    for a in answers:
        if a is None:
            strs += 'No '
        else:
            strs += 'Yes '

    print(strs)
