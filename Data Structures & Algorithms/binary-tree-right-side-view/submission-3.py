# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def DFS(self,node,level):

        if node is None:
            return

        if level in self.hashmap:
            self.hashmap[level].append(node.val)
        else:
            self.hashmap[level]=[node.val]

        if node.left:
            self.DFS(node.left,level+1)
        if node.right:
            self.DFS(node.right,level+1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.hashmap={}
        self.DFS(root,0)
        ans=[]
        for i in self.hashmap:
            print()
            ans.append(self.hashmap[i][-1])

        return ans
        