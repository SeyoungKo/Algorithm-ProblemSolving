# Symmetric Tree
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        queue = deque([root.left, root.right])

        while queue:
            cur_left = queue.popleft()
            cur_right = queue.popleft()
            if not cur_left and not cur_right:
                continue
            if not cur_left or not cur_right:
                return False
            if cur_left.val != cur_right.val:
                return False
            queue.append(cur_left.left)
            queue.append(cur_right.right)

            queue.append(cur_left.right)
            queue.append(cur_right.left)
        return True

if __name__ == '__main__':
    # root = [1, 2, 2, '', 3, '', 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # root = TreeNode(1)
    # root.right = TreeNode(2)
    # root.left = TreeNode(2)
    # root.left.right = TreeNode(2)
    # root.right.right = TreeNode(3)

    s = Solution()
    print(s.isSymmetric(root))