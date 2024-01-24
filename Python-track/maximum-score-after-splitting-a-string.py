class Solution: 
    def maxScore(self, s: str) -> int:
        new=list(map(int,s))
        zeros=1 if new[0]==0 else 0
        ones=1 if new[0]==1 else 0
        maxi=0  
        prefix=list(accumulate(new))
        for i in range(1,len(new)):
            zeros=i-prefix[i-1] 
            ones=prefix[-1]-prefix[i-1] 
            maxi=max(maxi,(zeros+ones))
      
        
        return maxi















        # new=list(map(int,s))
        # total=0  
        # prefix=[]
        # ans=-float('inf')
        # prefix=list(accumulate(new)) 
        # ones=prefix[-1]
        # zero = 1 if s[0]==0 else 0

        # for i in range (1,len(prefix)):
        #     ones-=prefix[i-1]
        #     zero=(len(new))-prefix[i] 
        #     total=ones+zero
        #     ans= max(ans,total) 
   
        # return ans

        