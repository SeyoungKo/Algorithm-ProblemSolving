# Sort Array By Parity (905)

class Solution:
    def sortArrayByParity(self, nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
        return nums

if __name__ == '__main__':
    nums = [0]
    s = Solution()
    print(s.sortArrayByParity(nums))