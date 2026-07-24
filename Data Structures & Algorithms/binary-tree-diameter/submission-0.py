# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res = max(left + right, res)
            return max(left, right) + 1
        helper(root)
        return res