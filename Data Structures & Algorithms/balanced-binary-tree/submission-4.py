# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Were gonna set an outside flag here to return
        flag = True
        def max_height(root):
            nonlocal flag
            #If we reach an end return 0
            if root is None:
                return 0
            #get right and left recursive subtree
            right_tree_depth = max_height(root.right)
            left_tree_depth = max_height(root.left)

            #In any case if we find a difference of depths we mark our flag
            if abs(right_tree_depth - left_tree_depth) > 1:
                flag = False
            
            #Regular return of the max of subtrees + 1, current depth
            return max(right_tree_depth, left_tree_depth) + 1
        max_height(root)
        #We return out flag
        return flag

        #Time complexity O(n), space O(h) for recursion, where h is height of tree.


