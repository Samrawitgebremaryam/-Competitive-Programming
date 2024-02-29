# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root,val):
            if not root:
                return 
            if not root.left and not root.right: 
                nonlocal ans

                ans += val + root.val
            else:
                value = val + root.val
                dfs (root.left,value*10)
                dfs (root.right,value*10)
        dfs(root,0)
        return ans 



                
        