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
        
        print(f"Slow {slow.val}")
        
        right = None
        cur = slow
        while cur:
            cur.next, cur, right = right, cur.next, cur

        print(f"Right {right.val}")
        
        cur = head
        left = head.next
        l_or_right = False
        while cur is not slow:
            print(cur.val if cur else None)
            if l_or_right:
                print("LEFT")
                cur.next = left
                left = left.next
                print(cur.next.val if cur.next else None, left.val if left else None)
            else:
                print("RIGHT")
                cur.next = right
                right = right.next
                print(cur.next.val if cur.next else None, right.val if right else None)
            l_or_right = not l_or_right
            cur = cur.next
        head = cur
            