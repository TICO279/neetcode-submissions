# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        result = []

        if root is None:
            return result
        #we start our queue with the root
        queue = deque([root])

        while queue:
            #We wanna process by levels
            #So we need a for loop of the length of the queue
            level_len = len(queue)
            #And somewhere to store the level nodes
            level = []
            
            for _ in range(level_len):
                #We grab our node
                node = queue.pop()
                #We add it to our level
                level.append(node.val)

                #We then for this specific node we append the childeen to the queue for the next level
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            #Once we finish the level
            result.append(level)

        return result


