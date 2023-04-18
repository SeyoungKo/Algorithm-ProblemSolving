if __name__ == '__main__':
    a = "1010"
    b = "1011"

    print(bin(int(a,2) + int(b,2))[2:]) # byte를 int로 변환하고 연산 후 2진수로 변환