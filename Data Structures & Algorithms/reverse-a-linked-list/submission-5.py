# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        cur = prev.next
        i = 1
        while(cur):
            saveNext = cur.next
            cur.next = prev
 
            prev = cur         
            cur = saveNext
            i+=1

        head.next = None
        head = prev

        return head
