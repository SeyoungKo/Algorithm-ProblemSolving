# Same Tree (100)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        # 같으면 true, 다르면 false 반환
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = [1, 2, 3]
    q = [1, 2, 3]

    p_tree = TreeNode(p, None, None)
    q_tree = TreeNode(q, None, None)

    solution = Solution()
    print(solution.isSameTree(p_tree, q_tree))

