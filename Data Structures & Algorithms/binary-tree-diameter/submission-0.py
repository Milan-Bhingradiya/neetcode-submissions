# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans=0
    def explore(self,root):
        if root is None:
            return 0
        
        left=0
        right=0
        if root.left is not None:
            left=left+self.explore(root.left)+1

        if root.right is not None:
            right=right+self.explore(root.right)+1

        if (left+right)>self.ans:
            self.ans=left+right

        return max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.explore(root)
        return self.ans
        