# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0

        prev = ListNode(0)
        head = prev

        while(l1 or l2):

            l1num = l1.val if l1 else 0
            l2num = l2.val if l2 else 0

            sum = l1num + l2num + remainder

            remainder = sum // 10
            new_val = sum % 10

            new_node = ListNode(new_val)
            prev.next = new_node
            prev = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if remainder!=0:
            prev.next = ListNode(remainder)

        head = head.next

        return head
            
        