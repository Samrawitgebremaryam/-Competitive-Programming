class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr=final=customers.count('Y')
        ans=0
        for i, val in enumerate (customers):
            curr+=-1 if val =="Y" else 1
            if final>curr:
                final=curr
                ans=i+1
        return ans 