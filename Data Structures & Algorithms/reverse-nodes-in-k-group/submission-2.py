# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ret_node = None
        dummy = ListNode(0, head)
        node = checkpoint = head
        i = 1
        while node:
            if i == k:
                if not ret_node:
                    ret_node = node
                dummy.next = node
                prv = node.next
                cur = checkpoint
                while cur and i != 0:
                    cur.next, prv, cur = prv, cur, cur.next
                    i -= 1
                node = checkpoint
                checkpoint = node.next
                dummy = node
            node = node.next
            i += 1
        return ret_node