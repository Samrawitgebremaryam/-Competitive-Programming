# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[]
        def inorder (root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)

        inorder(root)
        print(ans)
        total=0 

        for i in range (len(ans)):
            if ans[i]>=low and ans[i]<=high:
                total+=ans[i]
            if i>high:
                break
                
        return total
