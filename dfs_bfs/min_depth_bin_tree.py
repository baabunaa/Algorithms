# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q, level = [root], 0
        while q:
            size = len(q)
            level += 1
            for i in range(size):
                node = q.pop(0)
                if not node.left and not node.right: return level
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return level