# Truncate Sentence (1816)

class Solution:
    def truncateSentence(self, s, k):
        '''
        :param s: string
        :param k: int
        :return: string
        '''
        return ' '.join(s.split(' ')[:][0:k])

if __name__ == '__main__':
    strs = 'What is the solution to this problem'
    k = 4
    s = Solution()
    print(s.truncateSentence(strs, k))