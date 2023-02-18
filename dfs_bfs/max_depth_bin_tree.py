# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def help(root, count):
            if not root: return count
            if not root.left and not root.right: return count
            count += 1
            return max(help(root.left, count), help(root.right, count))

        return help(root, 1)