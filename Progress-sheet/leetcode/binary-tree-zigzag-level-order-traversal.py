# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=0
        leveldict=defaultdict(list)
        ans=[]
        def preorder (root,level):
            if root :  
                leveldict[level].append(root.val)
                preorder(root.left,level+1)
                preorder(root.right,level+1)
        preorder(root , level )
        
        for key,val in leveldict.items():
            if key%2==0:
                ans.append(val)
            else :
                ans.append(val[::-1])   
                   
        return ans 
