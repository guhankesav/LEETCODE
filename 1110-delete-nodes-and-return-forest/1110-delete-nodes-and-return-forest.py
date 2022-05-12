class Solution:
    def delNode(self,root)->TreeNode:
        if not root:
            return None
        root.left=self.delNode(root.left)
        root.right=self.delNode(root.right)
        if root.val in self.delete_vals:
            if root.left:
                self.res.append(root.left)
            if root.right:
                self.res.append(root.right)
            return None
        return root
        
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.delete_vals=set(to_delete)
        self.res=[]
        root=self.delNode(root)
        if root:
            self.res.append(root)
        return self.res