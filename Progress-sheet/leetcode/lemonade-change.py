class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=c10=c20=0
        for r in range (len(bills)):
            if bills[r]==5:
                c5+=1
            elif bills[r]==10:
                c10+=1
                if c5==0:
                    return False 
                c5-=1
            else:
                c20+=1
                if c5==0:
                    return False
                c5-=1
                if c10==0 :
                    if c5>=2 :
                        c5-=2 
                    else :
                        return False
                else:  
                    c10-=1 
        return True 
        