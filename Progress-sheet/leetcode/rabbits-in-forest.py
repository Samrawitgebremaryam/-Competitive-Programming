class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for ans,cnt in count.items():
            res+=((ans+1)*(ceil(cnt/(ans+1))))
        return res