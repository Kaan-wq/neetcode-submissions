# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = None
        cur = slow
        while cur:
            cur.next, cur, right = right, cur.next, cur
        
        left = head
        while right.next:
            nxt1, nxt2 = left.next, right.next
            left.next = right
            right.next = nxt1
            left, right = nxt1, nxt2