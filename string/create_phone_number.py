# Create Phone Number

class Solution:
    def create_phone_number(self, n):
        '''
        :param n: list
        :return: string
        '''
        str_n = ''.join([str(num) for num in n])

        return '({}) {}-{}'.format(str_n[:3], str_n[3:6], str_n[6:])


if __name__ == '__main__':
    s = Solution()
    print(s.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))