# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        local_count = 0
        value = 0
        
        def dfs(root):
            nonlocal local_count
            nonlocal value

            if root is None:
                return

            #We explore left side
            dfs(root.left)

            #We increment per node we process
            local_count += 1

            #We check if that node is the kth smallest
            if local_count == k:
                value = root.val
                return
            
            #We then process right as in order traversal
            dfs(root.right)

        
        dfs(root)


        return value
            

        