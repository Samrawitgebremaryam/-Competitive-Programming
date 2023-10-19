class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumetric=""
        for char in s:
            if char.isalnum():
                alphanumetric+=char
        alphanumetric_lower=alphanumetric.lower()
        if alphanumetric_lower==alphanumetric_lower[::-1]:
            return True
        else:
            return False
      
     
