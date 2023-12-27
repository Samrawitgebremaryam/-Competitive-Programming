class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros=0
        ans=[]

        result={}
        result[len(nums)] = nums.count(0)
        onces=nums.count(1)
        result[0] = onces
        for i in range (1, len(nums)):
            if nums[i-1]==0:
                zeros+=1
            else:
                onces-=1
            result[i] = zeros + onces

        maxi=max(result.values())
        for key,value in result.items():
            if value==maxi:
                ans.append(key)
        return ans

