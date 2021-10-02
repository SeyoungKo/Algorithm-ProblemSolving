# Disemvowel Trolls
import re

class Solution:
    def disemvowel(self, string_):
        '''
        :param string_: string
        :return: string
        '''
        # re.sub(검색패턴 - 문자열, 리스트, 치환 문자열, 대상)
        return re.sub(r'[aeiouAEIOU]', '', string_)

if __name__ == '__main__':
    strs = 'This website is for losers LOL!'
    s = Solution()
    print(s.disemvowel(strs))