class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maxno=nums[0]
        presum=[]
        pre=0
        for i in range(len(nums)):
            maxno=max(maxno,nums[i])
            a=nums[i]+ maxno
            pre+=a
            presum.append(pre)
        return presum
        