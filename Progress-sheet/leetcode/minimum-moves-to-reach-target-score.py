class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans =0
     
        while target>1 and maxDoubles >0:
            if target % 2==0:
                ans+=1
                maxDoubles-=1
                target//=2
               
            else:
                target-=1
                ans+=1        
        return ans+target-1
        


            













        # while x<target :
        #     if maxDoubles!=0:
        #         x=2*x
        #         maxDoubles-=1
        #         ans+=1
        #     else:
        #         ans+=(target-x)
        #         x+=(target-x)
                
        # return ans 

        