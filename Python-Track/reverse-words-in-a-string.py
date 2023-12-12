class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split()
        result=[]
        for i in range (len(res)-1,-1,-1):
            result.append(res[i])
        return " ".join(result)
        
        
        
        
        
        
        
        # l,r=len(s)-1,len(s)-1
        # result=''
        # while (l>-1):
        #     if s[l]!=" ":
        #         l-=1
        #     else:
        #         result+=s[l:r+1]
        #         r=l
        #         l-=1
        # result+=s[l:r] 
        # return result


        



        