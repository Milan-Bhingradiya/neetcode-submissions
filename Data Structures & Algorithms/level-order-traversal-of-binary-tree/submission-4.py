# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        ans=[]
        while queue:
            len_q=len(queue)
            sub_ans=[]
            for i in range(len_q):
                element=queue.popleft()
                if element:
                    sub_ans.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
            if sub_ans:
                ans.append(sub_ans)
        
        return ans
            
