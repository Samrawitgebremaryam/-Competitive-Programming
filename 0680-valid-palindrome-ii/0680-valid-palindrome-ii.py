class Solution(object):
    def validPalindrome(self, s):
        l,r =0, len(s)-1
        while l<r:
            if s[l]==s[r]:
                l,r=l+1,r-1
            else:
                one=s[:l]+s[l+1:]
                two=s[:r]+s[r+1:]
                if one==one[::-1] or two==two[::-1]:
                    return True 
                else :
                    return False
        return True


