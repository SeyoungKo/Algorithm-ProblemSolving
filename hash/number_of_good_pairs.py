# Number of Good Pairs (1512)

class Solution:

    def numIdenticalPairs(self, nums):
        dicts = {}
        cnt = 0

        for num in nums:
            if num in dicts:
                cnt += dicts[num]
                dicts[num] += 1
            else:
                dicts[num] = 1
        return cnt

if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    s = Solution()
    print(s.numIdenticalPairs(nums))