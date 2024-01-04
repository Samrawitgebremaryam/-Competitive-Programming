class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range (len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r] == -nums[i]:
                    ans.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]<-nums[i]:
                    l+=1
                else: 
                    r-=1 
        return list(ans)



        