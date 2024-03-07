class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            total = 0
            for p in piles:
                total += math.ceil(float(p) / k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    #    r =  max(piles)
    #    l =0 

    #    while l + 1 < r :
    #        myk = (l+r)//2

    #        total = 0 
    #        ans = 0
    #        for i in range (len (piles)):
    #            total += piles[i]
    #            if total == myk:
    #                ans +=1
    #                total = 0 
    #            elif total > myk :
    #                ans += ceil(piles[i]/ myk)
    #                total = piles[i]

    #        if total != 0 :
    #            ans += 1 

    #        if ans <= h :
    #            r = myk 
    #        else:
    #            l = myk

    #    return r

