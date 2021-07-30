# Same Tree (100)
from collections import deque

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


class Solution2:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return True

    def bfs(self, p, q):
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not self.isSameTree(p, q): # false
                return False
            if p or q:
                queue.append((p.left, q.left))
                queue.append((p.right, p.right))
        return True

if __name__ == '__main__':
    p = [1, 2, 3]
    q = [1, 2, 3]

    p_tree = TreeNode(p, None, None)
    q_tree = TreeNode(q, None, None)

    solution = Solution()
    print(solution.isSameTree(p_tree, q_tree))

    solution2 = Solution2()
    print(solution2.bfs(p_tree, q_tree))

