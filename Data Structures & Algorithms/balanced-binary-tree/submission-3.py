# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def max_height(root):
            nonlocal flag
            if root is None:
                return 0
            
            right_tree_depth = max_height(root.right)
            left_tree_depth = max_height(root.left)

            if abs(right_tree_depth - left_tree_depth) > 1:
                flag = False
            
            return max(right_tree_depth, left_tree_depth) + 1
        max_height(root)
        return flag


