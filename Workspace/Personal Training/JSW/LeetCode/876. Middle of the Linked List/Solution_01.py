# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_runner = head
        fast_runner = head
        while True:
            if fast_runner.next != None:
                fast_runner = fast_runner.next
                if fast_runner.next != None:
                    fast_runner = fast_runner.next
                else:
                    return slow_runner.next
            else:
                return slow_runner

            slow_runner = slow_runner.next
        
        return None