# Squares of a Sorted Array (977)
import math

class Solution:
    def sortedSquares(self, nums):
        sqrt_nums = [int(math.pow(num, 2)) for num in nums]
        return sorted(sqrt_nums)

if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    s = Solution()
    print(s.sortedSquares(nums))