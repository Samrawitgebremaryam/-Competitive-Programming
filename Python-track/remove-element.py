class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l,r=0,len(nums)-1
        
        
        # if len(nums)==1 and nums[0]==val:
        #     return 0
        # if len(nums)==0:
        #     return 0

        while l<=r:
            while r>=0 and  nums[r]==val:
                r-=1
        
            if nums[l]==val and r>l:
                nums[l],nums[r]=nums[r],nums[l]
        
            l+=1
        
        return r+1 
        