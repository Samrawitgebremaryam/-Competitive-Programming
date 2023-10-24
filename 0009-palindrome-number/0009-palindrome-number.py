class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        reversed=y[::-1]
        if y==reversed:
            return True
        else:
            return False
        
        