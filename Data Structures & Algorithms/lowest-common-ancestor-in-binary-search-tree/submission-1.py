# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans=None
    def explore(self,root,p,q):
        if root is None:
            return False

   
        left=self.explore(root.left,p,q)
        right=self.explore(root.right,p,q)

        print("left",left,"right",right)


        if left==True and right==True:
            self.ans=root
            return True
        elif (root.val==q.val or root.val==p.val) and left==True:
            self.ans=root
            return True
        elif (root.val==p.val or root.val==q.val) and right==True:
            self.ans=root
            return True
        elif (root.val==p.val or root.val==p.val) or root.val==q.val:
            return True

        return left or right 

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.explore(root,p,q)

        return self.ans