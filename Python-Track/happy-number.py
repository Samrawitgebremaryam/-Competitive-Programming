class Solution:
    def isHappy(self, n: int) -> bool:
        # summ = 0
        # for num in str(n):
        #     summ += pow(int(num), 2)
        # summ = sum([pow(int(x), 2)for x in str(n)])
        seen = set()
        while n != 1:
            summ = 0
            for num in str(n):
                summ += pow(int(num), 2)
            if summ in seen:
                return False
            seen.add(summ)
            n = summ
        return True       
        
        
            
        