# Reverse Prefix of Word (2000)

class Solution:
    def reversePrefix(self, word, ch):
        result = list()

        word[0], word[word.index(ch)] = word[word.index(ch)], word[0]
        word[1], word[2] = word[2], word[1]
        print(word)

if __name__ == '__main__':
    word = 'abcdefd'
    ch = 'd'
    s = Solution()
    print(s.reversePrefix(word, ch))