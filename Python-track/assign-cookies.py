class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        t,b=0,0
        
        while b<len(s) and t<len(g):
            if s[b]>=g[t]:
                t+=1
                b+=1
            else:
                b+=1
        return t

        