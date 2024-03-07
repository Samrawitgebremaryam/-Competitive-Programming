class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l , r = 0 ,max(nums)
        while l + 1 < r :
            print ( l, r)
            mid = (l + r) // 2 
            total=0 
            for i in range (len( nums)):
                total += ceil(nums[i]/mid) 
            
            if total <= threshold :
                r = mid
            else: 
                l = mid 
        return r 