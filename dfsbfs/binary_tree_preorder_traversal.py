# Binary Tree Preorder Traversal (144)
# 전위순회

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []
        def dfs(root):
            if root:
                result.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return result


if __name__ == '__main__':
    # root = [1, None, 2, 3]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    s = Solution()
    print(s.preorderTraversal(root))

