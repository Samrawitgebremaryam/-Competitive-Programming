class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1count=Counter(s1)
        k=len(s1)
        window=Counter(s2[:k])
        if window==S1count:
            return True 
        for i in range(len(s2)-k):
            window[s2[i]]-=1
            if window[s2[i]]==0:
                del window[s2[i]]
            window[s2[i+k]]+=1
            if window==S1count:
               return True 
        return False  