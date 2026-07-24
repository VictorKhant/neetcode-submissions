# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == p.val or node.val == q.val:
                return node
            if p.val < node.val and q.val < node.val:
                res = node.left
                stack.append(node.left)
            if p.val > node.val and q.val > node.val:
                res = node.right
                stack.append(node.right)
        return res