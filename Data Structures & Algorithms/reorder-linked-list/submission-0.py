# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #The first thing we wanna do is find the middle
        #for which we can do a two pointer approach O(n)

        if head == None or head.next == None:
            return
        
        slow = head
        fast = head
        
        #We found our middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #We save the middle
        middle = slow.next
        #And disconnect both lists
        slow.next = None
        

        #Now we should reverse the linked list from the middle to the end
        curr = middle
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #Now that we have the first half normal and the second half reversed
        #Were gonna modify putting one and one. 
        
        #For clarity lets remember our two halves heads
        
        #First half
        FH = head
        SH = prev
        

        while SH:
            #Save our next original values
            next_1_node = FH.next
            next_2_node = SH.next

            #Now append them to our solution
            FH.next = SH
            SH.next = next_1_node

            #Move our pointers
            FH = next_1_node
            SH = next_2_node
        














