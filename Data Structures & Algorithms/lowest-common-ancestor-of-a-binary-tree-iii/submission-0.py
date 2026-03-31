"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        cur = p
        while cur:
            seen.add(cur)
            cur=cur.parent
        cur = q
        while cur not in seen:
            cur = cur.parent
        return cur
        