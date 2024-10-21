# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur_l = node_l = ListNode(-1, None)
        cur_ge = node_ge = ListNode(-1, None)
        cur = head
        while cur != None:
            if cur.val < x:
                cur_l.next = cur
                cur_l = cur_l.next
            else:
                cur_ge.next = cur
                cur_ge = cur_ge.next
            cur = cur.next
        cur_l.next = node_ge.next
        cur_ge.next = None
        return node_l.next