class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        l=0
        total=0
        max_total=float(-inf)
        for r in range (n):
            total+=nums[r]
            if r>=k-1:
                max_total=max(total,max_total)
                total-=nums[l]
                l+=1
        avarage=max_total/k
        return avarage
            
              


            
        