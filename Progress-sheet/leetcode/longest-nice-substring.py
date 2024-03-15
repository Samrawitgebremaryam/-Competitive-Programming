class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice(word):
            letters=set(word)
            if len (word) < 2:
                return ''
            for i in range ( len ( word)) :
                if not (word[i].lower() in letters and word[i] .upper() in letters ):
                    word1=nice(word[:i])
                    word2= nice (word[i+1 :])
                    return word2 if len(word2) > len (word1) else word1 
            return word 
        return nice (s)
        
        
        

        
        