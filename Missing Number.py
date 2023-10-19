class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new=sorted(nums)
        missing=0
        for x in new:
            if x==missing:
                missing+=1
            else:
                return missing
        return len(new)
   
