# Goal Parser Interpretation (1678)

class Solution:
    def interpret(self, command):
        '''
        :param command: string
        :return: string
        '''
        return command.replace('()', 'o').replace('(al)', 'al')

if __name__ == '__main__':
    command = '(al)G(al)()()G'
    s = Solution()
    print(s.interpret(command))