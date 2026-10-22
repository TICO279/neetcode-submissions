# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Idea here, we can do a bfs, the ida is a top down approach, given we need to compare to previous nodes

#For a good node to proceed as good, it has to be bigger than the previous good node

#This can be done with a DFS

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current_count = 0
        if root:
            current_count +=1

        def dfs(root, last_good):
            nonlocal current_count
            #This is our base case
            if root is None:
                return

            if root.val >= last_good:
                last_good = root.val
                current_count += 1
            
            dfs(root.left, last_good)
            dfs(root.right, last_good)
        
        root_left = root.left
        root_right = root.right

        dfs(root_left, root.val)
        dfs(root_right, root.val)
        return current_count
        
        