class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        parent=self.kthGrammar(n-1,ceil(k/2))
        if k%2==0:
            return parent^1
        else:
            return parent
        
       
            
        #     if n == 1:
        #         return [0]
        #     prev= kth(n-1)
        #     row=[]
        #     for i in range (len(prev)):
        #         if prev[i]==0:
        #             row.append(0)
        #             row.append(1)
        #         else:
        #             row.append(1)
        #             row.append(0)
        #     return row
        # 


            