class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=defaultdict(int)
        count[0]=1
        ans=0
        prefix=list(accumulate(nums))
        for i in range (len(prefix)):
            if prefix[i]-goal in count:
                ans+=count[prefix[i]-goal]
            count[prefix[i]]+=1
        return ans 




        # l=ans=0
        # total=nums[l]
        # r=1
        # while l<r :
        #     total+=nums[r]
        #     if total==goal:
        #         ans+=1 
        #         if nums[l]==0:
        #             ans+=1
            
        #     elif total> goal:
        #         if nums[l]==1:
        #             total-=1
        #         l+=1
        #     r+=1 if r<len(nums) else 0
        # return ans 

        






        # ans=0
        # l=0
        # i=0 
        # prefix=list(accumulate(nums))
        # while l!=i or i<(len(prefix))-1:
        #     if prefix[i]==goal:
        #         ans+=1 
        #     if prefix[i]>goal:
        #         if nums[l]==1:
        #             ans+=1
        #             l+=1
        #     i+=1
          
        # return ans

     
        
