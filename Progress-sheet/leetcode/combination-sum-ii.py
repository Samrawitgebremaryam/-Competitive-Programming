class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       ans= []

       count=Counter(candidates)
       candidates = list(count.keys())
       
       def sum2 (i,path,target ):
            if i >= len(candidates):
                if target == 0:
                    ans.append(path)
                
                return

            if target <0:
                return 
            
            for j in range(count[candidates[i]]+1):
                
                sum2(i+1, path + [candidates[i]]*j, target-candidates[i]*j)
                
       sum2(0,[],target)
       return ans 