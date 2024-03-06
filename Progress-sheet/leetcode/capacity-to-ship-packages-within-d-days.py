class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights) - 1
        
        while l + 1 < r:
            capacity = (l+r)//2
            total = 0 
            ship = 0
            for i in range (len (weights)):
                total += weights[i]
                if total == capacity:
                    ship +=1
                    total = 0 
                elif total > capacity :
                    ship +=1
                    total = weights[i]


            if total != 0 :
                ship += 1 

            if ship <= days :
                r = capacity 
            else:
                l = capacity 

        return r





