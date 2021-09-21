# Defanging an IP Address (1108)

class Solution:
    def defangIPaddr(self, address):
        '''
        :param address: string
        :return: string
        '''
        for i in range(1, len(address)):
            if address[i] == '.':
                return address.replace('.', '[.]')

if __name__ == '__main__':
    address = "255.100.50.0"

    s = Solution()
    print(s.defangIPaddr(address))