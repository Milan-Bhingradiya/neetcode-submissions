# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge_two(self,l1,l2):

        if l1 and l2==None:
            return l1
        elif l1==None and l2:
            return l2

        dummy=ListNode()
        tail=dummy


        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
                tail=tail.next
            else:
                tail.next=l2
                l2=l2.next
                tail=tail.next
    
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists)==0:
            return None

        if len(lists)<2:
            return lists[0]
        

        while len(lists)>1:
            merged_list_heads=[]
            
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2= lists[i+1] if (i+1)<len(lists) else None
                merged_list_heads.append(self.merge_two(list1,list2))
            
            lists=merged_list_heads
                 
        return lists[0]
        