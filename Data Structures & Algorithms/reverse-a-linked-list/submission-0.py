# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        #While theres still an element
        while curr:
            #we save the original next to later continue
            next_node = curr.next
            #we then assign the next to the previous
            curr.next = prev
            #move our pointers
            prev = curr
            curr = next_node
        
        return prev