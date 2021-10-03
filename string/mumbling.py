# Mumbling

class Solution:
    def accum(self, strs):
        '''
        :param strs: string
        :return: string
        '''
        return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(strs))

if __name__ == '__main__':
    strs = "RqaEzty"
    s = Solution()
    print(s.accum(strs))