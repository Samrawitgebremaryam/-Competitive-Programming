class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        total=0
        max_v=1
        for r in range (len(nums)):
            total+=nums[r] 
            while (nums[r]*(r-l+1))-total>k: 
                total-=nums[l] 
                l+=1 
            max_v=max(max_v,r-l+1)  
        return max_v
        
                
       
        