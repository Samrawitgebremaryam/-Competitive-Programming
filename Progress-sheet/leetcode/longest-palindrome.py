class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=flag=0
        for val in count.values():
            if val%2==0:
                ans+=val
            else:
                ans+=val-1 
                flag+=1
        if flag>0 :
            return ans+1 
        else:
            return ans 








