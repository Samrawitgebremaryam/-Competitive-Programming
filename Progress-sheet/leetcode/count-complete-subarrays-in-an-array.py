class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total=len(set(nums))
        ans=l=0
        values=defaultdict(int)
        for r in range (len(nums)):
            values[nums[r]]+=1
            while len(values)==len(set(nums)):
                ans+=len(nums)-r
                values[nums[l]]-=1
                if values[nums[l]]==0:
                     values.pop(nums[l])
                l+=1
        return ans 


            

        