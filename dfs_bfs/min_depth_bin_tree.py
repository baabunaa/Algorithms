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
        stack = [root]
        count = 0
        while stack:
            count += 1
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                if not node.left and not node.right:
                    return count
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return count