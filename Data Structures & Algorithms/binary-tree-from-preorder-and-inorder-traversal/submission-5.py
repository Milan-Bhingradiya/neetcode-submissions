# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def make(self,l,r):
        if l>r:
            return None
        # print("l,r",l,r)
        val=self.preorder[self.curr_index]
        self.curr_index+=1
        root=TreeNode(val)
        mid=self.hashmap[val]
        root.left=self.make(l,mid-1)
        root.right=self.make(mid+1,r)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hashmap={}
        for idx,val in enumerate(inorder):
            self.hashmap[val]=idx
            
        self.n=len(preorder)-1
        self.preorder=preorder
        self.curr_index=0

        return self.make(0,self.n)

        