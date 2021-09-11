# Height Checker (1051)


class Solution:
    def heightChecker(self, heights):
        result = 0
        sort_height = sorted(heights)

        for i in range(len(sort_height)):
            if heights[i] != sort_height[i]:
                result += 1
        return result

if __name__ == '__main__':
    heights = [5,1,2,3,4]

    s = Solution()
    print(s.heightChecker(heights))