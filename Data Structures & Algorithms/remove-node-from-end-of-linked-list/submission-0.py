# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        curr =  head

        #If we have one node only
        if head.next is None:
            return None

        #Given that its backwards, lets reverse the list
        prev = None
        while curr:
            #Save the original next
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #We restart our pointer
        curr = prev

        #We have to check if its the first element
        if n == 1:
            curr2 = curr.next
            curr.next = None
        else:
            curr2 = curr

        #Reversed head
        rev_head = curr2

        #Lets first traverse to the nth element
        while curr2:
            if counter == n-2:
                #If we reached the element before the nth
                next_node = curr2.next
                curr2.next = next_node.next
                break
            else:
                
                curr2 = curr2.next
                counter +=1

        #Now we reverse back to get our original order from the last usable node
        curr = rev_head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev



