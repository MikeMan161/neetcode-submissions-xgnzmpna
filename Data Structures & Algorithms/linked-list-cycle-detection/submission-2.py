# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        pf = dummy
        ps = dummy
        while pf and pf.next:
            pf = pf.next
            if pf == ps:
                return True
            ps = ps.next
            pf = pf.next
        return False