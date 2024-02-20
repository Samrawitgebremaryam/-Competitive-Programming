class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i in range (len(s)):
            last[s[i]]=i
        end=l=0
        ans=[]
        for i in range (len(s)):
            end=max(end,last[s[i]])
            if i==end:
                ans.append (i-l+1)
                l=i+1
                end=0
        return ans  
            


