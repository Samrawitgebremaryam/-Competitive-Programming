class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def sum3(i,curset,n):
            if len(curset) == k and n == 0:
                ans.append(curset [:] )

            if n < 0:
                return 

            for j in range (i ,10):
                curset.append(j)
                sum3(j+1,curset,n-j)
                curset.pop()

        sum3(1,[],n)
        return ans 


        