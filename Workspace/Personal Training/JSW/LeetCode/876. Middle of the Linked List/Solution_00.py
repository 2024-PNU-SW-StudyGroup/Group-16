# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            n += 1
        result = head
        for i in range(n//2):
            result = result.next
        return result