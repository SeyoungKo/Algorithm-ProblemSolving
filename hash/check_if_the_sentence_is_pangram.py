# Check if the Sentence Is Pangram (1832)
from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence):
        '''
        :param sentence: string
        :return: bool
        '''
        alpha_list = list(ascii_lowercase)
        for alpha in alpha_list:
            if alpha not in list(sentence):
                return False
        return True

if __name__ == '__main__':
    sentence = "leetcode"
    s = Solution()
    print(s.checkIfPangram(sentence))