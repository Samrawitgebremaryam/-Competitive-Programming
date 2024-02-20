class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix=list(accumulate(nums))
        rem=prefix[-1]%p
        count={}
        count[0]=-1
        ans=len(nums)
        if rem==0: 
            return 0
        for i in range (len (prefix)):
            if (prefix[i]-rem)%p in count:
                ans=min(ans,i-count[(prefix[i]-rem)%p])
            count[prefix[i]%p]=i
        return -1 if ans ==len(nums) else ans 


