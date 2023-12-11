class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance=abs(target[0])+abs(target[1])
        for i in range (len(ghosts)):
            ghost=abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])
            if ghost<=distance:
                return False 
        return True 

        