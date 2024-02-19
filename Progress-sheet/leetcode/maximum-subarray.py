class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix=list(accumulate(nums))
        temp=0
        ans=float("-inf")
        for i in prefix:
            ans=max(ans,i-temp)
            if i<0:
                temp=min(temp,i)
            
        return ans 

   
     
        
        