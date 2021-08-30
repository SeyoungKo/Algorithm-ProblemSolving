# Relative Ranks (506)

import heapq

class Solution:
    def findRelativeRanks(self, score):
        heap = []
        heapq.heapify(heap)

        n = len(score)
        res = [n for _ in range(n)]

        for i, score in enumerate(score):
            heapq.heappush(heap, (-score, i))

        count = 0
        while heap:
            score, i = heapq.heappop(heap)
            count += 1
            if count == 1:
                res[i] = "Gold Medal"
            elif count == 2:
                res[i] = "Silver Medal"
            elif count == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(count)

        return res


if __name__ == '__main__':
    score = [5, 4, 3, 2, 1]
    s = Solution()
    print(s.findRelativeRanks(score))
