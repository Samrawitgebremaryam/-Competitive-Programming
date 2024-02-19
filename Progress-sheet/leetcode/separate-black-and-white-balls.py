class Solution:
    def minimumSteps(self, s: str) -> int:
        l=count=0
        for r in range (len(s)):
           
            if s[r]=='0':
                count+=r-l
                l+=1  

        return count 



            



        # l,r=0,1
        # count=0
        # s=list(s)

        # while r<len(s):
        #     if s[l]=='1'and s[r]=="0":
        #         s[l],s[r]=s[r],s[l]
        #         count+=1
        #     l+=1
        #     r+=1
        
        # return count 

        
        