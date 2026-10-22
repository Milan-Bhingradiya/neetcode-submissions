# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans_max=0

    def explore(self,root,depth):
        if root.left is None and root.right is None:
            self.ans_max=max(self.ans_max,depth)
            return

        if root.left is not None:
            self.explore(root.left,depth+1)
        
        if root.right is not None:
            self.explore(root.right,depth+1)

   
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.explore(root,1)

        return self.ans_max
      