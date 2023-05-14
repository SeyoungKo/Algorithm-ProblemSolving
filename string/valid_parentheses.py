# Valid Parentheses

class Solution:
    def valid_parentheses(self, strs):
        '''
        :param strs: str
        :return: bool
        '''

        left, right = 0, 0
        for s in strs:
            if right > left:
                return False
            if s == '(':
                left += 1
            elif s == ')':
                right += 1

        return True if left == right else False

if __name__ == '__main__':
    strs = ")(()))"
    s = Solution()
    print(s.valid_parentheses(strs))