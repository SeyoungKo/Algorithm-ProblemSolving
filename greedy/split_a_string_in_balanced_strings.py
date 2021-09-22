# Split a String in Balanced Strings (1221)

class Solution:
    def balancedStringSplit(self, strs):
        '''
        :param strs: string
        :return: int
        '''
        count, track = 0, 0

        for s in strs:
            if s == 'R':
                track += 1
            else:
                track -= 1

            if not track: # track = 0
                count += 1

        return count

if __name__ == '__main__':
    strs = "RLRRLLRLRL"
    strs1 = "RLLLLRRRLR"
    strs2 = "LLLLRRRR"

    s = Solution()
    print(s.balancedStringSplit(strs2))