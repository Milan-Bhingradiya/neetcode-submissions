# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __init__(self):
        self.hashmap={}

    def DFS(self,root,level):
        if root is None:
            return
       
        if level in self.hashmap:
            self.hashmap[level].append(root.val)
        else:
            self.hashmap[level]=[]
            self.hashmap[level].append(root.val)
        # print(self.hashmap)
            
        self.DFS(root.left,level+1)
        self.DFS(root.right,level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.DFS(root,0)
        ans=[]
        for i in self.hashmap:
            ans.append(self.hashmap[i])

        return ans
            
