# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root== None: return ans
        queue = [root]
        flag = 0
        while queue:
            size = len(queue)
            temp = [0]*size
            for i in range(size):
                node = queue.pop(0)
                if flag==0:
                    temp[i] = node.val
                else:
                    temp[size-i-1] = node.val  
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(temp)
            flag^=1
        return ans