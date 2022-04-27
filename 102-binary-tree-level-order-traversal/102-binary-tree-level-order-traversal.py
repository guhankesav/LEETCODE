class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        ans = []
        level = [root]
        
        while level:
            
            ans.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        
        return ans