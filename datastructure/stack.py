# 스택 파이썬으로 구현하기
def stack():
    stack = []

    stack.append(5)
    stack.append(4)
    stack.append(3)
    stack.pop()
    stack.append(2)
    stack.append(1)
    stack.pop()

    print(stack[len(stack)-1])

    print(stack[::])
    print(stack[::-1]) #반대로 출력 (stack ver)
if __name__ == '__main__':
    stack()