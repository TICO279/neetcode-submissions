# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(root1, root2):
            nonlocal flag
            if root1 is None and root2 is None:
                return None

            if root1 is None and root2:
                flag = False
                return
            
            if root1 and root2 is None:
                flag = False
                return
            
            if root1.val != root2.val:
                flag = False
                return
            left_nodes = dfs(root1.left, root2.left)
            right_nodes = dfs(root1.right, root2.right)
        dfs(p,q)

        return flag
