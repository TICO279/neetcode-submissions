# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #we check if they are empty
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            curr1 = list1
            curr2 = list2

        #Were gonna first assign the head to return later
        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next

        #We initialize our current 3 node
        curr3 = head

        while curr1 and curr2:
            
            #Check scenarios of whos bigger
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            #Then move our curr3 pointer one more. 
            curr3 = curr3.next

        #we check and assign the remaining elements if we do have more. 
        if curr1:
            curr3.next = curr1
        else:
            curr3.next = curr2

        return head












