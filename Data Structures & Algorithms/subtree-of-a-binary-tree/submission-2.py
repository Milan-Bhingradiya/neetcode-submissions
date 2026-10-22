# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check_both(self,root,subroot):
        if root is None and subroot is None:
            return True
        
        if root is None or subroot is None:
            return False
        
        if root.val != subroot.val:
            return False
        
        left=self.check_both(root.left,subroot.left)
        right=self.check_both(root.right,subroot.right)

        return left and right

    def explore(self,root,subroot):
        if root is None:
            return False

        if root.val==subroot.val:
            ans= self.check_both(root,subroot)
            if ans==True:
                return True
            
        left=self.explore(root.left,subroot)
        right=self.explore(root.right,subroot)

        return left or right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.explore(root,subRoot)

