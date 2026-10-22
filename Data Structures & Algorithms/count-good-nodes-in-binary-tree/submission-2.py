# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,root,biggest):

        if root is None:
            return  
        
        if root.val>=biggest:
            biggest=root.val
            self.ans.append(root.val)

        self.DFS(root.left,biggest)
        self.DFS(root.right,biggest)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.ans=[]
        self.DFS(root,-float('inf'))
        # print(self.ans)
        return len(self.ans)
        