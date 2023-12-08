class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3="zxcvbnmZXCVBNM"
        
        for i in range (len (words)):
            new=set()
            for j in range (len (words[i])):
                if words[i][j] in row1:
                    new.add(1)
                elif words[i][j] in row2:
                    new.add(2)
                else:
                    new.add(3)
            if len(new)==1:
                res.append(words[i])
        return res


        