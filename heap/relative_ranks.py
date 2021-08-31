# Relative Ranks (506)
import heapq


class Solution:
    def findRelativeRanks_sort(self, score):
        g = sorted(score, reverse=True)
        d = {}
        m = []

        for i in range(len(g)):
            if i == 0:
                d[g[i]] = "Gold Medal"
            elif i == 1:
                d[g[i]] = "Silver Medal"
            elif i == 2:
                d[g[i]] = "Bronze Medal"
            else:
                d[g[i]] = str(i + 1)
        for i in score:
            m.append(d[i])
        return m

    def findRelativeRanks_heap(self, score):
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
    # score = [5, 4, 3, 2, 1]
    score = [10,3,8,9,4]
    s = Solution()

    print(s.findRelativeRanks_sort(score))
    print(s.findRelativeRanks_heap(score))
