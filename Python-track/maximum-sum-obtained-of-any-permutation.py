class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count=[0]*len(nums)
        ans=0
        for i in range(len(requests)):
            count[requests[i][0]]+=1
            if requests[i][1] <len(nums)-1:
                count[requests[i][1]+1]-=1 
        prefix=list(accumulate(count))
        nums.sort()
        prefix.sort()
        for i in range(len(nums)):
            ans+=prefix[i]*nums[i]
        return ans%(10**9+7)

            

        