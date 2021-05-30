# 피보나치 수 5 (10870번)

def fib(n):
    if n >= 2:
        return fib(n - 1) + fib(n - 2)
    elif n == 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    n = int(input())
    print(fib(n))