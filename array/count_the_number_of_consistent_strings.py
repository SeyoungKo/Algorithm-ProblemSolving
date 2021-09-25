# Count the Number of Consistent Strings (1684)

class Solution:
    def countConsistentStrings(self, allowed, words):
        '''
        :param allowed: string
        :param words: list
        :return: int
        '''
        allowed_list = list(set(allowed))
        count = 0

        for word in words:
            for letter in word:
                if letter not in allowed_list:
                    count += 1
                    break

        return len(words) - count

if __name__ == '__main__':
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    s = Solution()
    print(s.countConsistentStrings(allowed, words))