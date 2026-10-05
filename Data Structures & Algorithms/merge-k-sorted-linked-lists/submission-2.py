# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = len(lists)
        if count == 1: return lists[0]
        if count == 0: return None

        while count > 1:
            half = (count + 1) // 2
            for j in range(half):
                if j + half >= count: break
                a = lists[j]
                b = lists[j+half]
                dummy = ListNode()
                cur = dummy
                while a and b:
                    if a.val <= b.val:
                        cur.next = a
                        a = a.next
                    else:
                        cur.next = b
                        b = b.next
                    cur = cur.next
                cur.next = a or b
                lists[j] = dummy.next
            count = half
        return lists[0]