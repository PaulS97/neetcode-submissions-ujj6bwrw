# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def kMore(head, k) -> None:
            count = k
            while(head):
                count -= 1
                if count==0:
                    return head
                head = head.next
            return head

        def reverseList(head, k) -> ListNode:
            prev = None
            curr = head
            count = k
            while(count):
                count -= 1
                save = curr
                curr = curr.next
                save.next = prev
                prev = save

            #return prev

        k_tail = kMore(head, k)
        start = head
        prev = None

        if not k_tail:
            return head
        else:
            res = k_tail

        while(k_tail):
            next_start = k_tail.next

            reverseList(start, k)
            if prev:
                prev.next = k_tail
            
            prev = start
            start.next = next_start
            start = next_start
            k_tail = kMore(start, k)

        return res



                
            

            

        