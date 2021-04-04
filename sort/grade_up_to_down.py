# 성적이 낮은 순서로 학생 출력하기

def print_student(info):
    res = sorted(info, key=lambda x : x[1], reverse=True)

    for i in range(len(res)):
        print(res[i], end= ' ')


if __name__ == '__main__':
    n = int(input())
    names, grades = [], []

    for i in range(n):
        inputs = list(map(str, input().split()))
        names.append(inputs[0])
        grades.append(inputs[1])

    # dictinary comprehension
    dicts = {n : grades[i] for i, n in enumerate(names)}

    print_student(dicts)