class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique =set()
        l=0
        total=0
        max_total=-float("inf")
        for r in range (len(nums)):
            while nums[r] in unique:
                total-=nums[l]
                unique.remove(nums[l])
                l+=1
            unique.add(nums[r])
            total+=nums[r] 
            max_total=max(total,max_total)

        return max_total
           
                


        