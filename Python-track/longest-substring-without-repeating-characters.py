class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        length=0
        longest=0
        unique=set()
        for r in range (n):
            while s[r] in unique :
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            length=r-l+1
            longest=max(length,longest)
        
        return longest  
            
        