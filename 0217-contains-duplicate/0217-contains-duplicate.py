class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new=sorted(nums)
        l,r=0,1
        while r<len(new):
            if new[l]==new[r]:
                return True
            else: 
                r+=1
                l+=1
        return False
        