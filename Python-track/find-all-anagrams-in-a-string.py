class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count=Counter(p)
        k=len(p)
        s_count=Counter(s[:k])
        if s_count==p_count:
            count=[0]
        else:
            count=[]
        for i in range(k,len(s)):
            s_count[s[i]]+=1
            s_count[s[i-k]]-=1
            if s_count[s[i-k]]==0:
                s_count.pop(s[i-k])

            if s_count==p_count:
                count.append(i-k+1)
        return count 

        