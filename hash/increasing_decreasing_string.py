# Increasing Decreasing String (1370)
from collections import Counter

class Solution:
    def sortString(self, s):
        '''
        :param s: str
        :return: str
        1. 가장 작은 문자를 배열에 추가
        2. 1번보다 최소한 큰 문자 배열에 추가
        3. 더이상 추가할 문자가 없을때까지 2번 반복
        4. 가장 큰 문자 추가
        5. 4번보다 최소한 작은 문자 배열에 추가
        6. 더이상 추가할 문자가 없을때까지 5번 반복
        7. 1~6 반복
        '''

        result = list()
        cnt = dict(Counter(s))
        check = True

        while cnt:
            for dict_key in sorted(cnt) if check else reversed(sorted(cnt)):
                result.append(dict_key)
                cnt[dict_key] -= 1

                if cnt[dict_key] == 0:
                    del cnt[dict_key]
            check = False

        return ''.join(result)

if __name__ == '__main__':
    str = 'aaaabbbbcccc'

    s = Solution()
    print(s.sortString(str))