# Two Sum (1)


class Solution:
    def twoSum(self, nums, target):
        result = list()
        cur = target
        while nums:
            if target >= max(nums) and cur > 0:
                result.append(nums.index(max(nums)))
                val = nums.pop(nums.index(max(nums)))
                cur = cur - val
            elif cur <= 0:
                break
            else:
                _ = nums.pop(nums.index(max(nums)))
        return result

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    print(s.twoSum(nums, target))