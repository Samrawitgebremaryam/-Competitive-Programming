class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel="aeiou"
        count=0
        l=0
        n=len(s)
        max_count=float(-inf)
        for r in range (n):
            if s[r] in vowel:
                count+=1
            if r>=k-1:
                max_count = max(count,max_count)
                if s[l] in vowel:
                    count-=1
                l+=1
        return max_count


        