class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x + 1
        if x == 1 :
            return 1 
        while l + 1 < r :  
            mid = (l+r) // 2
            val= mid * mid 
            if val < x :
                l = mid   
            elif val > x: 
                r = mid 
            elif val == x :
                return mid 
        return l
            
        




        