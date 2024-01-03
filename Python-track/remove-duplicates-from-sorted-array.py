class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for r in range (len (nums)):
            if nums[l]!=nums[r] and l<len(nums)-1:
                nums[l+1],nums[r]=nums[r],nums[l+1]
                l+=1
        return l+1
            




        

        