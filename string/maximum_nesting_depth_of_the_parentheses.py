# Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s):
        '''
        :param s: string
        :return: int
        '''
        res = 0
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
            elif i == ")":
                cnt -= 1
            res = max(res, cnt)
        return res

if __name__ == '__main__':
    strs = "(1+(2*3)+((8)/4))+1"
    s = Solution()
    print(s.maxDepth(strs))