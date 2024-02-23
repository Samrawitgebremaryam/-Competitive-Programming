class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        index=deque() 
        for i in range(len(tickets)):
            index.append(i)

        ans=0
        while index and tickets[k]!=0:
            val=index.popleft()
            tickets[val]-=1
            ans+=1
            if tickets[val] !=0:
                index.append(val)

        return ans


        