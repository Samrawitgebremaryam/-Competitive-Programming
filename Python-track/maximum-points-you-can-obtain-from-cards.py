class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        total=sum(cardPoints)
        ksum=0
        ans=0
        max_total=-float("inf")
        if k==len(cardPoints) :
            return total 
        for r in range(len(cardPoints)):
            ksum+=cardPoints[r] 
            if r+1>=len(cardPoints)-k:
                ans=total-ksum
                max_total=max(max_total,ans)
                ksum-=cardPoints[l]
                l+=1
        return max_total



        