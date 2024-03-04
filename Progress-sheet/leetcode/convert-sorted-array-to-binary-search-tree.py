# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binarySearch(l,r):
            if l==r:
                return TreeNode(nums[r])
            if l>r :
                return 
            mid=(r+l)//2
            root=TreeNode(nums[mid])
            lefts=binarySearch(l,mid-1)
            rights=binarySearch(mid+1,r)
            root.left=lefts
            root.right=rights
            return root 
        return binarySearch(0,len(nums)-1)
