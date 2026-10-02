# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head.next if head else None
        fast = head.next.next if head and head.next else None
        while slow and fast:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return False