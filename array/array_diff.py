# Array.diff

class Solution:
    def array_diff(self, a, b):
        '''
        :param a: list
        :param b: list
        :return: list
        '''
        return [a_val for a_val in set(a) if a_val not in b]


if __name__ == '__main__':
    s = Solution()
    print(s.array_diff([1, 2, 2, 2, 3],[1, 2]))