# Decode XORed Array (1720)

class Solution:
    def decode(self, encoded, first):
        '''
        :param encoded: list
        :param first: int
        :return: list
        '''
        result = [first]

        for en in encoded:
            result.append(en^result[-1])
        return result

if __name__ == '__main__':
    encoded = [1, 2, 3]
    first = 1
    s = Solution()
    print(s.decode(encoded, first))