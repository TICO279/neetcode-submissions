# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #counter
        diameter = 0

        def max_Depth(root: Optional[TreeNode]) -> int:
            nonlocal diameter
            #This is our base case to return
            if root is None:
                return 0

            right_subtree_depth = max_Depth(root.right)
            left_subtree_depth = max_Depth(root.left)
            
            #Update our biggest diameter
            diameter = max(diameter, right_subtree_depth + left_subtree_depth)
            
            #Return regular depth of subtree
            return max(right_subtree_depth, left_subtree_depth)+1

        max_Depth(root)

        return diameter

    
