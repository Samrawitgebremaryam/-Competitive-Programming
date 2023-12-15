class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        not_ans=set()
        numbers=set(fronts+backs)
        for i in range(len(backs)):
            if fronts[i]==backs[i]:
                not_ans.add(fronts[i]) 
        ans=numbers-not_ans
        return min(ans) if ans else 0