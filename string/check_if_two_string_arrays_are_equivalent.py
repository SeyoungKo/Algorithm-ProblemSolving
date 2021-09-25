# Check If Two String Arrays are Equivalent (1662)

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        '''
        :param word1: list
        :param word2: list
        :return: bool
        '''
        return True if ''.join(word1) == ''.join(word2) else False

if __name__ == '__main__':
    word1 = ['ab', 'c']
    word2 = ['a', 'bc']

    s = Solution()
    print(s.arrayStringsAreEqual(word1, word2))