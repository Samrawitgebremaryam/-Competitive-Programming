class Solution:
    def balancedString(self, s: str) -> int:
        ans = len(s)  
        count =Counter(s) 
        l = 0  
        for i, letter in enumerate(s):
            count[letter] -= 1  
            while l < len(s) and all(count[letter] <= len(s) // 4 for letter in 'QWER'):
                ans = min(ans, i - l + 1)  
                count[s[l]] += 1 
                l += 1  
     
        return ans  