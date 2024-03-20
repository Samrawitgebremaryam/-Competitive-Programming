# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs (root , cur_min , cur_max):
            if not root :
                return cur_max - cur_min
            cur_min = min ( cur_min , root.val)
            cur_max = max (cur_max , root.val )

            return max(dfs(root.left , cur_min ,cur_max), dfs(root.right , cur_min ,cur_max))
   
        return dfs(root , root.val , root.val)