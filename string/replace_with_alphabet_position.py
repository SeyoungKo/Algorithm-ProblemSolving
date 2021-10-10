# Replace With Alphabet Position
from string import ascii_lowercase
import re

class Solution:
    def alphabet_position(self, text):
        '''
        :param text: str
        :return: str
        '''
        nums = dict()
        for i, letter in enumerate(ascii_lowercase):
            nums[letter] = i + 1

        return ' '.join([str(nums[letter]) for letter in re.sub(r'[^a-zA-Z]', '', text.lower())])

if __name__ =='__main__':
    strs = "The sunset sets at twelve o' clock."
    s = Solution()
    print(s.alphabet_position(strs))