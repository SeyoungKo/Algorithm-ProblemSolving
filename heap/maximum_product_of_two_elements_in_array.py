# Maximum Product of Two Elements in an Array (1464)

import heapq

class Solution:
    def maxProduct(self, nums):
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))

        while heap:
            if len(heap) >= 2:
                top1 = heapq.heappop(heap)[1]
                top2 = heapq.heappop(heap)[1]
                return (top1-1) * (top2-1)

if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    s = Solution()
    print(s.maxProduct(nums))