# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If fast reaches the end, no cycle
        return False