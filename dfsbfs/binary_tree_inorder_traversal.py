# Binary Tree Inorder Traversal (94)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []

        while True:
            # left를 모두 stack에 append
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return result

            node = stack.pop()
            result.append(node.val)
            # left 모두 탐색 후 right를 모두 stack에 append
            root = node.right

    # DFS recursion
    def dfs_recursive(self, root):
        result = []

        def dfs_recursion(root):
            if root:
                dfs_recursion(root.left)
                result.append(root.val)
                dfs_recursion(root.right)

        dfs_recursion(root)
        return result


if __name__ == '__main__':
    # root = [1, None, 2, 3]

    root = TreeNode(1)
    root.left = TreeNode(None)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    # print(s.inorderTraversal(root))
    print(s.dfs_recursive(root))