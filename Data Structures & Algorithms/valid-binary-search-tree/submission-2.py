# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        import math
        queue = deque([(root, -math.inf, math.inf)])

        #Were gonna perform a regular BFS
        while queue:
            node, lower_bound, upper_bound = queue.pop()

            if node.left:
                left = node.left
                if left.val >= node.val or left.val <= lower_bound:
                    return False
                else:
                    queue.appendleft((left, lower_bound, node.val))
            
            if node.right:
                right = node.right
                if right.val <= node.val or right.val >= upper_bound:
                    return False
                else:
                    queue.appendleft((right, node.val, upper_bound))
        
        return True
