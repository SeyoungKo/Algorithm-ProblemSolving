# 문자열 압축
# 압축할 문자열 s가 주어질 때 1개 이상 단위의 문자열을 잘라 압축해 표현한 문자열 중 가장 짧은 것의 길이 구하기
if __name__ == '__main__':
    print('input : ', end='')
    input_str = input()
    answer = len(input_str)

    # 문자열을 압축할 수 있는 모든 방법을 수행한다.
    for i in range(1, len(input_str) // 2 + 1): # 최대 n/2번까지
        count = 1
        compress_str = ''
        iter_str = input_str[0:i]

        for j in range(i, len(input_str), i): # i만큼 stride
            if iter_str == input_str[j:j + i]:
                count += 1
            else: # 이전과 다른 문자열이 나왔다면
                if count >= 2: # 이전에 반복이 있었다면
                    compress_str += str(count) + iter_str
                else:
                    compress_str += iter_str # 반복이 없으면 숫자를 출력하지 않는다.

                iter_str = input_str[j:j + i] # 현재 위치로 초기화
                count = 1 # count 초기화

        # 남아있는 문자열 처리
        if count >= 2:
            compress_str += str(count) + iter_str
        else:
            compress_str += iter_str

        answer = min(answer, len(compress_str))
    print(answer)