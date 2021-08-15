# Remove Duplicates from Sorted Array (26)
# O(1)
class Solution:
    def removeDuplicates(self, nums):
        cnt = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[cnt] = nums[i + 1]
                cnt += 1
        return cnt

    def removeDuplicates2(self, nums):
        nums[:] = set(nums)
        return len(nums)

if __name__ == '__main__':
    input_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(s.removeDuplicates(input_arr))
    print(s.removeDuplicates2(input_arr))
