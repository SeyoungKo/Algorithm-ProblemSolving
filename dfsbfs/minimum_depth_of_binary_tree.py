# Minimum Depth of Binary Tree (111)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            if root:
                if not root.left and not root.right:
                    return depth
                else:
                    queue.append((root.left, depth + 1))
                    queue.append((root.right, depth + 1))


if __name__ == '__main__':
    # root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode('')
    root.left.right = TreeNode('')
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(2)
    # root.left = TreeNode(None)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(None)
    # root.right.right = TreeNode(4)
    # root.right.right.left = TreeNode(None)
    # root.right.right.right = TreeNode(5)
    # root.right.right.right.left = TreeNode(None)
    # root.right.right.right.right = TreeNode(6)

    s = Solution()
    print(s.minDepth(root))