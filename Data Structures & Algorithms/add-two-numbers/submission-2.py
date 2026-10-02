# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, l1)
        prev, q = None, 0
        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            q, r = (val_l1 + val_l2 + q) // 10, (val_l1 + val_l2 + q) % 10
            if l1:
                l1.val = r
            else:
                l1 = ListNode(r, None)
                prev.next = l1
            prev = l1
            l1 = l1.next
            l2 = l2.next if l2 else None

        if q > 0:
            prev.next = ListNode(q, None)
        
        return dummy.next