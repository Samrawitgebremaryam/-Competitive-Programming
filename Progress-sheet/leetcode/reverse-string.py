class Solution:

    def reverseString(self, s: List[str]) -> None:
        def rev(l,r):
            if l>=r:
                return
            s[l],s[r]=s[r],s[l]
            return rev(l+1,r-1)
        return  rev(0,len(s)-1)
    
        """
        Do not return anything, modify s in-place instead.
        """
        