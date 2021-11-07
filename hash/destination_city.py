# Destination City (1436)

class Solution:
    def destCity(self, paths):
        '''
        :param paths: list
        :return: str
        '''
        # hash
        graph = {source: destination for source, destination in paths}

        source = paths[0][0]
        current = source

        while current in graph:
            current = graph[current]
        return current

if __name__ == '__main__':
    paths = [["B","C"], ["D","B"], ["C","A"]]
    s = Solution()
    print(s.destCity(paths))