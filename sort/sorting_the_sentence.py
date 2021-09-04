# Sorting the Sentence (1859)

class Solution:
    def sortSentence(self, s):
        words = s.split(' ')[:]
        res = sorted(words, key=lambda x: int(x[-1]))
        result = [res[i][:-1] for i in range(len(res))]
        return ' '.join(result)

if __name__ == '__main__':
    sentence = "is2 sentence4 This1 a3"
    s = Solution()
    print(s.sortSentence(sentence))