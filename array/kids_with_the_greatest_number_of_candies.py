# Kids With the Greatest Number of Candies (1431)

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        '''
        :param candies: list
        :param extraCandies: int
        :return: list
        '''
        result = [True if candy + extraCandies >= max(candies) else False for candy in candies]
        return result

if __name__ == '__main__':
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    s = Solution()
    print(s.kidsWithCandies(candies, extraCandies))