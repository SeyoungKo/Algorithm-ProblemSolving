# Replace All Digits With Caracters (1844)
from string import ascii_lowercase

class Solution:
    def replaceDigits(self, s):
        '''
        :param s: string
        :return: string
        '''
        result = list()
        for i, letter in enumerate(s[:-1]):
            for j, alphabet in enumerate(ascii_lowercase):
                if alphabet == letter:
                    result.append(alphabet)
                    result.append(ascii_lowercase[j + int(s[i+1])])

        if s[-1] in ascii_lowercase:
            result.append(s[-1])

        return ''.join(result)

if __name__ == '__main__':
    strs = 'a1b2c3d4e'
    s = Solution()
    print(s.replaceDigits(strs))