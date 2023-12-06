class Solution:
    def freqAlphabets(self, s: str) -> str:
        word=''
        i = len(s)-1
        while i>-1:
            if s[i]!='#':
                word+=chr(96+int(s[i]))
                i-=1
            else:
                word+=chr(96+int(s[i-2:i]))
                i-=3
        return word[::-1]
        
        
            

           