class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def heat (radius) :
            a , b  = 0 , 0
            while a < len ( houses ) and b < len (heaters) :
                if abs(houses[a] - heaters[b] ) <= radius :
                    a += 1 
                else:
                    b +=1 
            if a < len (houses) : 
                return False 
            else: 
                return True

        l, r = -1 , 10 ** 9 
        while l + 1 < r :
            mid = (l+r) // 2
            if heat(mid) :
                r = mid 
            else:
                l = mid 
        return r


     