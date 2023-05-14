# The Supermarket Queue

class Solution:
    def queue_time(self, customers, n):
        '''
        :param list:
        :param int:
        :return: int
        '''

        l = [0] * n
        for i in customers:
            l[l.index(min(l))] += i
        return max(l)

if __name__ == '__main__':
    customers = [1, 2, 3, 4, 5]
    n = 1

    s = Solution()
    print(s.queue_time(customers, n))