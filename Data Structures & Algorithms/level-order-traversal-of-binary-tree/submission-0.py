# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        #Result
        result = []
        
        #If the root is none
        if root is None:
            return result
        
        #We start our queue with root
        queue = deque([root])

       

        while queue:
            #We need to see how many nodes we have at this level to repeat
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                #We take the node in queue
                node = queue.popleft()
                #Then add it to the current level
                current_level.append(node.val)

                #Now we check left and right as thats level order traversal
                #These will be the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #Once the current level is finished, we append that level to the result
            result.append(current_level)
        return result


