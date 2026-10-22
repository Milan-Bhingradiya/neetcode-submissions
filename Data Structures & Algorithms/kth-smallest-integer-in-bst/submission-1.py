# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,root):
        if root is None:
            return
        
        self.DFS(root.left)
        self.ans.append(root.val)
        self.DFS(root.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=[]
        print(self.ans)
        self.DFS(root)

        return self.ans[k-1]
        