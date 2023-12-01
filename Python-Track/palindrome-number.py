class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums=str(x)
        l,r=0,len(nums)-1
        while(l<r):
            if nums[l]==nums[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        