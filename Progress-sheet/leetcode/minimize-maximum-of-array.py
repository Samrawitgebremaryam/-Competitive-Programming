class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxi=0
        total=0
        for i in range (len(nums)):
            total+=nums[i]
            maxi=max(maxi,ceil(total/(i+1)))
            
        return maxi 

        
            
          
        