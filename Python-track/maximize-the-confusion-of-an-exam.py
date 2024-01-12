class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        trues = 0
        falses = 0
        diff=0
        length=0
        for r in range (len(answerKey)):
            if answerKey[r]=="T":
                trues+=1
            else:
                falses+=1
            
            while min(trues,falses) >k:
                if answerKey[l]=="T":
                    trues-=1
                else:
                    falses-=1 
                l+=1
            length=max(length,r-l+1)
        return length
             

        