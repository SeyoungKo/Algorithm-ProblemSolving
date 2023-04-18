# Array Partition (561)

class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    s = Solution()
    s.arrayPairSum(nums)