# Who like this?

class Solution:
    def likes(self, names):
        case = {
            0: 'no one likes this',
            1: '{} likes this',
            2: '{} and {} like this',
            3: '{}, {} and {} like this',
            4: '{}, {} and {others} others like this'
        }
        # *args : 여러개 아규먼트가 들어올 때 튜플로 처리한다
        # **kwargs : 여러개 key=value로 입력할 때 딕셔너리로 처리한다.
        return case[min(len(names), 4)].format(*names, others=len(names)-2)

if __name__ == '__main__':
    '''
    [] -->  "no one likes this"
    ["Peter"] -->  "Peter likes this"
    ["Jacob", "Alex"] -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"] -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"] -->  "Alex, Jacob and 2 others like this"
    '''

    names = ["Alex", "Jacob", "Mark", "Max", 'test1', 'test2', 'test3']
    s = Solution()
    print(s.likes(names))