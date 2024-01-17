class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans=[]
        total=0
        temp=list(s)
        prefix=[0]*len(s)
        for l in range (len(shifts)):
            if shifts[l][2] == 0:
                prefix[shifts[l][0]]-=1
                if shifts[l][1]<len(s)-1:
                    prefix[shifts[l][1]+1]+=1
                
            else:
                prefix[shifts[l][0]]+=1
                if shifts[l][1]<len(s)-1:
                    prefix[shifts[l][1]+1]-=1
            
        
        for i in range (len(prefix)):
            total+=prefix[i]
            ans.append(total)
        print(ans)
        for i in range(len(temp)) :
            temp[i]=chr(((ord(temp[i])+ans[i]-96)%26 or 26) +96)
        return "".join(temp) 



        