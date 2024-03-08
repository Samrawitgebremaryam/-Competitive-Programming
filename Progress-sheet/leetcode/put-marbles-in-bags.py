class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        part=[]

        for i in range ( len (weights)-1):
            part.append(weights[i]+weights[i+1])

        part.sort()
        k=k-1
        i=mini=maxi=0 
        while i < k:
            mini += part[i]
            maxi += part[len(part)-1-i]
            i+=1

        return maxi-mini 
        