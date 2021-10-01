# Decrypt String from Alphabet to Integer Mapping (1309)
from string import ascii_lowercase

class Solution:
    def freqAlphabets(self, s):
        alphabet = dict()
        for i, letter in enumerate(ascii_lowercase[:9]):
            alphabet[i + 1] = letter

        for i, letter in enumerate(ascii_lowercase[9:]):
            alphabet[str(i + 10) + '#'] = letter

        s_list = s.replace('#', ' ').split(' ')
        if len(s_list[0]) >= 3:
            s_list.append(s_list[0][-2])

        return alphabet

if __name__ == '__main__':
    strs = '10#11#12'
    strs2 = '1326#'
    s = Solution()
    print(s.freqAlphabets(strs))
    print(s.freqAlphabets(strs2))