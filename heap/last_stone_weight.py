# Last Stone Weight (1046)
# x == y : 둘다 삭제
# x != y : x는 없어지고 y-x한 값만 남음
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones] # 최대 힙으로 만들기
        heapq.heapify(stones)

        while len(stones) > 1:
            top = abs(heapq.heappop(stones))
            top2 = abs(heapq.heappop(stones))
            if top != top2:
                heapq.heappush(stones, abs(top2 - top))
        return stones[0] if len(stones) >= 1 else 0


if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(s.lastStoneWeight(stones))