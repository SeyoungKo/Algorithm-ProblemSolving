# To Lower Case (709)

class Solution:
    def toLowerCase(self, s):
        '''
        :param s: string
        :return: string
        '''
        return s.lower()

if __name__ == '__main__':
    strs = 'LOVELY'
    s = Solution()
    print(s.toLowerCase(strs))