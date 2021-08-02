# Maximum Depth of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root)) # depth, object

        while stack:
            cur_depth, root = stack.pop()
            print(f'root is {root}')
            if root is not None:
                stack.append((cur_depth + 1, root.left))
                stack.append((cur_depth + 1, root.right))

        return cur_depth

if __name__ == '__main__':
    # root = [3, 9, 20, None, None, 15, 7]
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(s.maxDepth(root))