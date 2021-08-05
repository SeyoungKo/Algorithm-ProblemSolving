# Binary Tree Postorder Traversal (145)
# 후위순회

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        result = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                result.append(root.val)

        dfs(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(None)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.postorderTraversal(root))