# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = ListNode()
        p2 = ListNode()
        p1 = head
        p2 = head

        while p2:
            p2 = p2.next
            if p1 == p2:
                return True
            if not p2:
                return False
            p2 = p2.next
            p1 = p1.next
        return False