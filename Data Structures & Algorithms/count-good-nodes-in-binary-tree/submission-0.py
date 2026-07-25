# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currmax):
            if not root:
                return 0
            stack = [root]
            while stack:
                node = stack.pop()
                if node and node.val >= currmax:
                    return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
                return dfs(node.left, currmax) + dfs(node.right, currmax)
        return dfs(root, float('-inf'))
        
            
        