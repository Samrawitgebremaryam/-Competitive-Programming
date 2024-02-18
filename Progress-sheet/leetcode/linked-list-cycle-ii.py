# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        look=set()
        while curr:
            if curr in look :
                return curr 
            look.add(curr)
            curr=curr.next
        return None