# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def max_depth(root):
            return max(max_depth(root.left),max_depth(root.right)) + 1 if root else 0
        
        over_root = max_depth(root.left) + max_depth(root.right)        
        return max(over_root, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        