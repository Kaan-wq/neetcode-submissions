"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        dummy = Node(0)

        cur, cur_new = head, dummy
        while cur:
            node = Node(cur.val)
            nodes[cur] = node
            cur_new.next = node
            cur, cur_new = cur.next, cur_new.next

        cur, cur_new = head, dummy.next
        while cur:
            cur_new.random = nodes[cur.random] if cur.random else None
            cur, cur_new = cur.next, cur_new.next
        return dummy.next
