# Check if All Characters Have Equal Number of Occurrences
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s):
        '''
        :param s: string
        :return: bool
        '''
        count = dict(Counter(s))
        key = count[s[0]]

        for v in count.values():
            if v != key:
                return False
        return True

if __name__ == '__main__':
    str = 'aaabb'

    s = Solution()
    print(s.areOccurrencesEqual(str))