# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        

        # base case
        if not root:
            return 0
        
        queue = [root]
        depth = 1
        while queue:
            
            children = []
            for node in queue:
                
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            
            queue = children
            depth += 1