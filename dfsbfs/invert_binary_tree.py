# Invert Binary Tree (226)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        result = []
        queue = deque([(root)])

        while queue:
            cur = queue.popleft()
            if cur:
                tmp = cur.left
                cur.left = cur.right
                cur.right = tmp

                result.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)

        return result

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    s = Solution()
    print(s.invertTree(root))