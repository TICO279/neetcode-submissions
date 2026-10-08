# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #This is our base case
        if root is None:
            return None
        
        #We then swap our value
        root.left, root.right = root.right, root.left

        #And recursively compute the rest left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        #Then we simply return the root. 
        return root
