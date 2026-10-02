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
        
        cur = head
        left = head.next
        l_or_right = False
        while cur is not slow:
            if l_or_right:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            l_or_right = not l_or_right
            cur = cur.next    