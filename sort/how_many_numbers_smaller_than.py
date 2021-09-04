# How Many Numbers Are Smaller Than the Current Number (1365)

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i, n in enumerate(nums):
            cnt = 0
            for j, val in enumerate(nums):
                if i == j:
                    continue
                if n > val:
                    cnt += 1
            result.append(cnt)

        return result

if __name__ == '__main__':
    nums = [7, 7, 7, 7]

    s = Solution()
    print(s.smallerNumbersThanCurrent(nums))