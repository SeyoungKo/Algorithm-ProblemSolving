# Maximum Product Difference Between Two Pairs (1913)

class Solution:
    def maxProductDifference(self, nums):
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

if __name__ == '__main__':
    nums = [5, 6, 2, 7, 4]
    s = Solution()
    print(s.maxProductDifference(nums))