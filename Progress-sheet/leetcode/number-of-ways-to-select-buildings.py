class Solution:
    def numberOfWays(self, s: str) -> int:
        once=ans=0
        zeros=0
        oneZero=[0]*(len(s)+1)
        zeroOne=[0]*(len(s)+1)
        for i in range (len(s)):
            if s[i]=='0':
                zeros+=1
                oneZero[i+1]=once
            else:
                once+=1
                zeroOne[i+1]=zeros
            oneZero[i+1]+=oneZero[i]
            zeroOne[i+1]+=zeroOne[i]
        
        for i in range (len (s)):
            if s[i]=='0':
                ans+=zeroOne[i]
            else:
                ans+=oneZero[i]
        return ans 


        
      
        