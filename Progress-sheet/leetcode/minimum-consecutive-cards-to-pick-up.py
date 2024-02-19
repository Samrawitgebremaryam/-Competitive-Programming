class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card={}
        dis =float("inf")
        for i in range (len(cards)):
            if cards[i] in card :
                dis =min(i-card[cards[i]]+1, dis)
            card[cards[i]]=i
            
        return -1 if dis ==float("inf") else dis 
            











        # card =set()
        # dis=0
        # l=0
        # for r in range (len(cards)):
        #     if cards[r] in card:
        #         dis=min(dis,r-l+1)
        #         l+=1
        #     else:
        #         dis+=1

        # return dis 

