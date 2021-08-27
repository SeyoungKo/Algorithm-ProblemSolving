# The K Weakest Rows in a Matrix (1337)

import heapq

class Solution:
    def kWeakestRows(self, mat, k):
        print(sum(mat[1]))
        vals = [-sum(m) for m in mat]
        heap, cnt = [], 0
        result = []

        for i, val in enumerate(vals):
            heapq.heappush(heap, (-val, i))

        while k >= 1:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result

if __name__ == '__main__':
    mat = [[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]]

    k = 3
    s = Solution()
    print(s.kWeakestRows(mat, k))