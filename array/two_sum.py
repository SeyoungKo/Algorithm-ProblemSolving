# Two Sum (1)


class Solution:
    def twoSum(self, nums, target):
        check = {}
        for i,num in enumerate(nums):
            if num not in check:
                check[target-num]=i
            else:
                return [min(i,check[num]),max(i,check[num])]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    print(s.twoSum(nums, target))