# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return (None,0)
            left_node, left_count = dfs(node.left)
            right_node,right_count = dfs(node.right)
            mid = 1 if node == p or node == q else 0
            total = left_count + right_count + mid
            if node == p or node==q:
                return (node,total)
            if left_node and right_node:
                return (node,total)
            return (left_node or right_node, total)
        ans,count= dfs(root)
        return ans if count == 2 else None