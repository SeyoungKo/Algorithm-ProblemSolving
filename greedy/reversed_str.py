# 문자열 뒤집기
# 0과 1로 이루어진 문자열 s가 주어질 때 모두 같은 숫자로 만들 수 있는 최소 횟수를 출력한다.


if __name__ == '__main__':
    print('input: ', end='')
    input_str = str(input())
    count0, count1 = 0, 0

    if input_str[0] == '1':
        count1 += 1
    else:
        count0 += 1

    # 2번째부터 확인
    for i in range(len(input_str)-1):
        if input_str[i] != input_str[i+1]:
            if input_str[i] == '1':
                count1 += 1
            else:
                count0 += 1

    print(min(count1, count0))