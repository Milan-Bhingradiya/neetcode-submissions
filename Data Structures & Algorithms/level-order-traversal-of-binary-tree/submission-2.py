
class Solution:
    def __init__(self):
        self.ans=[]
        self.queue=deque()
  
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root is None:
        return []

      self.queue.append(root)
      self.queue.append(None)

      while len(self.queue)>0:
        # print("queue",len(self.queue))
        # for i in self.queue:
        #   print(i.val if i!=None else None, end=" ")

        print()         
        subans=[]
        element=self.queue.popleft()

        while element!=None:
          subans.append(element.val)
          if element.left!=None:
            self.queue.append(element.left)
          if element.right!=None:
            self.queue.append(element.right)
          element=self.queue.popleft()

          
        if element==None and len(self.queue)!=0:
          self.queue.append(element)

        self.ans.append(subans)

      return self.ans