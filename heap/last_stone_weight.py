# Last Stone Weight (1046)

import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_node = abs(heapq.heappop(stones))
            second_node = abs(heapq.heappop(stones))
            if first_node != second_node:
                heapq.heappush(stones, -abs(first_node - second_node))
        return abs(stones[0]) if len(stones) >= 1 else 0

if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(s.lastStoneWeight(stones))