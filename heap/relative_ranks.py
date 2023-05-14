# Relative Ranks (506)
import heapq


class Solution:
    def findRelativeRanks_sort(s다elf, score):
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

        result = [_ for _ in range(len(score))]

        cnt = 0
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))

        while heap:
            idx = heapq.heappop(heap)[1]
            cnt += 1
            if cnt == 1:
                result[idx] = 'Gold Medal'
            elif cnt == 2:
                result[idx] = 'Silver Medal'
            elif cnt == 3:
                result[idx] = 'Bronze Medal'
            else:
                result[idx] = cnt

        return result

if __name__ == '__main__':
    # score = [5, 4, 3, 2, 1]
    score = [10,3,8,9,4]
    s = Solution()

    print(s.findRelativeRanks_sort(score))
    print(s.findRelativeRanks_heap(score))