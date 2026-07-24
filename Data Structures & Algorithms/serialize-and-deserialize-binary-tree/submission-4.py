# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        que = deque([root])
        res = ''
        while que:
            node = que.popleft()
            res += str(node.val) + ' ' if isinstance(node, TreeNode) else node + ' '
            if not isinstance(node, TreeNode):
                continue
            if node.left:
                que.append(node.left)
            else:
                que.append('N')
            if node.right:
                que.append(node.right)
            else:
                que.append('N')
        return res
        
            #         1
            #     2
            # 4       5
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        lst = data.split()
        lst.reverse()
        if not lst:
            return None
        head = TreeNode(lst.pop())
        que = deque([head])
        while lst:
            node = que.popleft()
            l, r = lst.pop(), lst.pop()
            if l != "N":
                node.left = TreeNode(int(l))
                que.append(node.left)
                
            if r != "N":
                node.right = TreeNode(int(r))
                que.append(node.right)

        return head
       

            

            
                
            
            
