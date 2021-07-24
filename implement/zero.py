# 제로

if __name__ == '__main__':
    count = int(input())
    stack_ = []

    for i in range(count):
        num = int(input())
        if num == 0:
            stack_.pop()
        else:
            stack_.append(num)

    print(sum(stack_))
