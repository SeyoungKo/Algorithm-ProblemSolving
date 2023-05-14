# Count the Number of Consistent Strings (1684)

class Solution:
    def countConsistentStrings(self, allowed, words):
        '''
        :param allowed: string
        :param words: List
        :return: integer
        '''
        allowed = list(set(allowed))
        cnt = 0

        for word in words:
            for letter in word:
                if letter not in allowed:
                    cnt += 1
                    break

        return len(words) - cnt

if __name__ == '__main__':
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]

    s = Solution()
    print(s.countConsistentStrings(allowed, words))
