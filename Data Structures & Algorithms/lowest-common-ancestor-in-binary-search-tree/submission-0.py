# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #For our base case
        if root is None:
            return None
        
        #if at some point we find q or p, thats our LCA
        if root.val == q.val:
            return q
        if root.val == p.val:
            return p

        #If our root is bigger than our target nodes
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        
        #If our root is smaller
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)

        #The cases where its in between, we just return the root. 
        return root



