# Concatenation of Array (1929)

class Solution:
    def getConcatenation(self, nums):
        '''
        :param nums: list
        :return: list
        '''
        return nums + nums

if __name__ == '__main__':
    nums = [1, 3, 2, 1]
    s = Solution()
    print(s.getConcatenation(nums))