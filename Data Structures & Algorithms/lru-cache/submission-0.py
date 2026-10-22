class Node:
    def __init__(self,key,val=0,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        # left means lease used
        self.left=Node(0,0)
        #right means max used
        self.right=Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def insert_at_right(self,node):
        prev=self.right.prev
        prev.next=node
        node.next=self.right
        node.prev=prev
        self.right.prev=node

        

    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        

    def get(self, key: int) -> int:

        if key in self.cache:
            # get kayro means used to put at right side delete then add o(1)
            node=self.cache[key]
            self.remove(node)
            self.insert_at_right(node) 
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        # add first then remove the guy who used less from left
        if key in self.cache:
            self.remove(self.cache[key])

        node=Node(key,value)
        self.insert_at_right(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            node=self.left.next
            self.remove(node)
            del self.cache[node.key]

