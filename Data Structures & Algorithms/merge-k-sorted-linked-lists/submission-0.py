# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def printList(self, head):
        print("[ ", end="")
        while(head):
            print(head.val, end="")
            head = head.next
        print("]")

    def mergeLists(self, one, two) -> listNode:
       # print("merging:", self.printList(one), self.printList(two))
        head = ListNode()
        curr = head
        while(one and two):
            if one.val < two.val:
                curr.next = one
                one = one.next
            else:
                curr.next = two
                two = two.next
            curr=curr.next

        if one:
            curr.next = one
        else:
            curr.next = two

        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeLists(lists[0], lists[1])
        else:
            mid = (0 + len(lists)-1)//2
            lists1 = lists[0:mid]
            lists2 = lists[mid:len(lists)]
           # print("mid: ", mid)
           # print("listlen:", len(lists1), len(lists2))
            return self.mergeLists(self.mergeKLists(lists1), self.mergeKLists(lists2))

        


                 

        


        