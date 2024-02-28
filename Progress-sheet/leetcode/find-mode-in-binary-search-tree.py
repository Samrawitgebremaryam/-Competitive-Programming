# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=defaultdict(int)
        def countfre (root):
            if root :
                count[root.val]+=1
                countfre(root.left)
                countfre(root.right)
        countfre(root)
        maxi=0
        ans=[]
        for val ,fre in count.items():
            if fre>maxi:
                maxi=fre
        for val ,fre in count.items():
            if fre==maxi:
                ans.append(val)
        return ans 

            

            
