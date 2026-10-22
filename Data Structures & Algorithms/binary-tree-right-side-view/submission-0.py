# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        #Lets put somewhere to save our result
        result = []

        if root is None:
            return result
        
        queue = deque([root])

        while queue:
            #We still need to remember the level length
            level_length = len(queue)

            for i in range(level_length):
                node = queue.pop()
                if i == level_length-1:
                    result.append(node.val)
                
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

        return result

