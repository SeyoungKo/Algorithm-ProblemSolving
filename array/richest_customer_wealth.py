# Richest Customer Wealth (1672)

class Solution:
    def maximumWealth(self, accounts):
        '''
        :param accounts: list
        :return: int
        '''
        values = [sum(account) for account in accounts]
        return max(values)

if __name__ == '__main__':
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    s = Solution()
    print(s.maximumWealth(accounts))