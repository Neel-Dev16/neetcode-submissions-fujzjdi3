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
        if not head:
            return None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt

        # Step 2: assign random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: separate
        curr = head
        copy_head = head.next
        copy = copy_head

        while curr:
            curr.next = curr.next.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
            copy = copy.next

        return copy_head