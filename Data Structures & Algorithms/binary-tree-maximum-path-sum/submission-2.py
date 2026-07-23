# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root):
            nonlocal res

            l = dfs(root.left) if root.left else 0
            r = dfs(root.right) if root.right else 0
            half = max(l, r) + root.val
            full = l + r + root.val
            if res < max(half, full, root.val):
                res = max(half, full, root.val)
            return max(root.val, half)
        _ = dfs(root)
        return res
