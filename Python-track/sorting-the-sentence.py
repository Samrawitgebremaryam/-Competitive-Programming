class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        ans=[]
        s.sort(key=lambda x:x[-1])
        for i in s:
            ans.append(i[:-1]) 
        return " ".join(ans)
        