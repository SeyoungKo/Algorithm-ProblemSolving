# Jewels and Stones (771)

class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewels = set(jewels)
        cnt = 0

        for item in stones:
            if item in jewels:
                cnt += 1

        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.numJewelsInStones('aA', 'aAAbbbb'))