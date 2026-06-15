# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # first split lists


        fast = head
        slow = head
        steps = 0

        while(fast and fast.next):
            steps += 1
            slow = slow.next
            fast = fast.next.next

       # print("steps:", steps)
        #print("slow:", slow.val)
        

        def reverse_list(head) -> ListNode:
            prev = None
            curr = head

            while(curr):
                save = curr
                curr = curr.next
                save.next = prev
                prev = save

            head = prev

            return head

        tail = reverse_list(slow)

        curr = head
        up = tail

        #print("up:", up.val)

        while up:
           # print("curr:", curr.val)
            save = curr.next
            curr.next = up
            curr = up
            up = save

        curr.next = None






            



                


