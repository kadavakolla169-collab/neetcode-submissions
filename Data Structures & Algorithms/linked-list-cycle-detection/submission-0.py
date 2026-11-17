# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head
        visited = set()
        while curr_node:
            if curr_node in visited:
                return True
            visited.add(curr_node)
            curr_node = curr_node.next
        return False