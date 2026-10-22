# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,root,l,r):

        if root is None:
            return True
        
        if root.val<=l or root.val>=r:
            return False
       
        a=self.DFS(root.left,l,root.val)
        b=self.DFS(root.right,root.val,r)

        return a and b
       
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        return self.DFS(root,-float('inf'),float('inf'))
        