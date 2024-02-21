class Solution:
    def minAddToMakeValid(self, s: str) -> int:
       opening=0
       close=ans=0
       for i in range(len(s)):
           if s[i]=="(":
               opening+=1
           else:
                if opening!=0:
                    opening-=1
                else:

                    ans+=1
       return ans + opening 

        

       
       
       
       
        # count=Counter(s)
        # return abs(count['(']-count[')'])
        
        