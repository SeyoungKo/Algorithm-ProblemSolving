# Running Sum of 1d Array (1480)

class Solution:
    def runningSum(self, nums):
        '''
        :param nums: string
        :return: list
        '''
        result = list()
        total = 0
        for n in nums:
            total += n
            result.append(total)

        return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print(s.runningSum(nums))