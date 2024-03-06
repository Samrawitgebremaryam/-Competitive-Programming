# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n
        while l+1 < r :
            mid=(l+r)//2
            if isBadVersion(mid) :
                r=mid
            else:
                l=mid 
        return r 
        # while l<=r:
        #     mid=(l+r)//2
        #     if  isBadVersion(mid) :
        #         if  not isBadVersion(mid-1):
        #             return mid 
        #         r=mid-1 
        #     else:
        #         l=mid+1

                
        
    
        