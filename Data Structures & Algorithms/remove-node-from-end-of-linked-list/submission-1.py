# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        pfast = head
        pslow = dummy
        pslow.next = head
        x = 0
        if not pfast.next:
            return head.next
        while x < (n-1):
            pfast = pfast.next
            x += 1
        while pfast.next:
            pslow = pslow.next
            pfast = pfast.next
        pslow.next = pslow.next.next
        return dummy.next

        