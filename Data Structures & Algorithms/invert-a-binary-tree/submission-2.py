# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sub(self,root):
        if root is None:
            return

        temp=root.left
        root.left=root.right
        root.right=temp
        self.sub(root.left)
        self.sub(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sub(root)
        return root
        