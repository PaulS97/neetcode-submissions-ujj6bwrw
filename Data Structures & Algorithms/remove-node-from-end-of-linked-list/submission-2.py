# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        prev = None
        curr = head
        while(curr.next):
            prev = curr
            curr = curr.next
            size += 1

        if n == size:
            head = head.next
            return head

        if n == 1:
            prev.next = None
            return head
        
        back_n = size - n  
        counter = 1

        prev = None
        curr = head

        print("size:", size)
       

        while(counter<=back_n):
            prev = curr
            curr = curr.next
            counter += 1

        prev.next = curr.next

        return head

        

        
        