class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(start,path, target):
            if target==0:
                ans.append(path[:])
            
            if target <0:
                return 

            for i in range (start,len(candidates)):
                path.append(candidates[i]) 
                combination(i,path,target-candidates[i])
                path.pop()  
        ans = []
        combination(0,[],target)
        return ans      
            
            
        
