class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0 
        zero=0
        max_value=0
        for r in range (len(nums)):
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1 
            max_value=max(max_value,r-l)
        return max_value

            

        