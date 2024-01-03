class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       
        count=Counter(nums)
        value=0
        new=list(set(nums))
        new.sort()
        l,r=0,len(new)-1
        while r>=0:
            value+=(count[new[r]]*(r-l))
            r-=1
        return value



        