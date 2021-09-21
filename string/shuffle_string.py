# Shuffle String (1528)

class Solution:
    def restoreString(self, s, indices):
        '''
        :param s: string
        :param indices: list
        :return: string
        '''
        sorted_list = {idx: s[i] for i, idx in enumerate(indices)}
        res = sorted(sorted_list.items(), key=lambda x: x[0])
        return ''.join([r[1] for r in res])

if __name__ == '__main__':
    strs = 'codeleet'
    indices = [4,5,6,7,0,2,1,3]

    s = Solution()
    print(s.restoreString(strs, indices))