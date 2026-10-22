# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    all_ok=True

    def explore(self,root):
        if root is None:
            return 0
        
        left=0
        right=0

        if root.left is not None:
            left=left+self.explore(root.left)+1
        
        if root.right is not None:
            right=right+self.explore(root.right)+1

        if abs(left-right)>1:
            self.all_ok=False
        
        return max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.explore(root)

        if self.all_ok:
            return True
        else:
            return False
        