# Make Two Arrays Equal by Reversing Sub-arrays (1460)
from collections import Counter

class Solution:
    def canBeEqual(self, target, arr):
        return Counter(target) == Counter(arr)

if __name__ == '__main__':
    target = [3, 7, 9]
    arr = [3, 7, 11]

    s = Solution()
    print(s.canBeEqual(target, arr))